// Diagnose, do not modify: locate per-bone linear-acceleration peaks at 60 and 120 Hz.
// Uses the original GLB and the isolated coach lab. No generated clip is written or activated.
const { chromium } = require('@playwright/test');
const fs = require('node:fs');
const path = require('node:path');

(async () => {
  const browser = await chromium.launch({
    executablePath: process.env.CHROMIUM_PATH,
    args: ['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader']
  });
  try {
    const page = await browser.newPage();
    await page.route('**/*', async route => {
      const name = new URL(route.request().url()).pathname.replace(/^\//, '');
      const allowed = name === 'tools/coach-lab.html' ||
        name === 'assets/coach/coach.glb' ||
        name === 'vendor/three.module.js' ||
        name === 'vendor/loaders/GLTFLoader.js';
      if (!allowed) return route.abort();
      return route.fulfill({
        body: fs.readFileSync(name),
        contentType: name.endsWith('.js') ? 'text/javascript' :
          name.endsWith('.html') ? 'text/html' : 'application/octet-stream'
      });
    });
    await page.goto('http://motion.internal/tools/coach-lab.html?once=1');
    await page.waitForFunction(() => window.ready);
    const report = await page.evaluate(() => {
      const output = [];
      for (const clip of lab.clips) {
        for (const hz of [60, 120]) {
          lab.select(clip.name);
          const dt = 1 / hz;
          const count = Math.round(clip.duration * hz);
          let previous = null;
          let previousVelocity = null;
          const peaks = new Map();
          for (let frame = 0; frame <= count; frame++) {
            const time = Math.min(frame * dt, clip.duration);
            const current = lab.skeleton(time);
            if (previous) {
              const velocity = {};
              for (const [name, joint] of Object.entries(current)) {
                const before = previous[name].position;
                velocity[name] = joint.position.map((value, axis) => (value - before[axis]) / dt);
              }
              if (previousVelocity) {
                for (const [name, vector] of Object.entries(velocity)) {
                  const prior = previousVelocity[name];
                  const acceleration = Math.hypot(...vector.map((value, axis) => (value - prior[axis]) / dt));
                  const entry = peaks.get(name) || { bone: name, peak: 0, time: 0 };
                  if (acceleration > entry.peak) {
                    entry.peak = acceleration;
                    entry.time = time;
                  }
                  peaks.set(name, entry);
                }
              }
              previousVelocity = velocity;
            }
            previous = current;
          }
          output.push({
            exercise: clip.name,
            duration: clip.duration,
            sampleHz: hz,
            highestJointPeaks: [...peaks.values()].sort((a, b) => b.peak - a.peak).slice(0, 20)
          });
        }
      }
      return output;
    });
    const target = 'docs/development/motion-review/joint-diagnostics.json';
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, JSON.stringify({
      method: 'World-space bone-origin linear acceleration; finite differences; 60 and 120 Hz; diagnostic only, not a safety or biomechanical metric.',
      source: 'Original coach.glb; no candidate loaded or changed.',
      exercises: report
    }, null, 2));
    for (const item of report.filter(x => x.exercise === 'jumpingjacks')) {
      console.log(JSON.stringify(item));
    }
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exit(1); });
