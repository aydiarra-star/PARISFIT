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
    const diagnostics = { pageErrors: [], consoleErrors: [], failedRequests: [], served: [] };
    page.on('pageerror', error => diagnostics.pageErrors.push(error.stack || error.message));
    page.on('console', message => {
      if (message.type() === 'error') diagnostics.consoleErrors.push(message.text());
    });
    page.on('requestfailed', request => diagnostics.failedRequests.push({
      url: request.url(), error: request.failure()?.errorText || 'unknown'
    }));
    await page.route('**/*', async route => {
      const url = new URL(route.request().url());
      const name = url.pathname.slice(1);
      const allowed = name === 'tools/coach-lab.html' ||
        name === 'assets/coach/coach.glb' ||
        name.startsWith('vendor/three/');
      if (!allowed) {
        diagnostics.failedRequests.push({ url: route.request().url(), error: 'blocked by diagnostic allowlist' });
        return route.abort();
      }
      try {
        const body = fs.readFileSync(name);
        diagnostics.served.push({ path: name, bytes: body.length });
        return route.fulfill({
          body,
          contentType: name.endsWith('.js') ? 'text/javascript' :
            name.endsWith('.html') ? 'text/html' : 'application/octet-stream'
        });
      } catch (error) {
        diagnostics.failedRequests.push({ url: route.request().url(), error: error.message });
        return route.abort();
      }
    });
    await page.goto('http://motion.internal/tools/coach-lab.html?once=1', { waitUntil: 'load' });
    try {
      await page.waitForFunction(() => window.ready === true, { timeout: 45000 });
    } catch (error) {
      const state = await page.evaluate(() => ({
        ready: window.ready === true,
        hasLab: !!window.lab,
        title: document.title,
        body: document.body?.innerText?.slice(0, 1000)
      })).catch(e => ({ evaluationError: e.message }));
      console.error('COACH_LAB_BOOT_FAILURE', JSON.stringify({ state, diagnostics }, null, 2));
      throw new Error('Coach lab did not initialize; see COACH_LAB_BOOT_FAILURE above. ' + error.message);
    }
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
          const ranked = [...peaks.values()].sort((a, b) => b.peak - a.peak);
          const bodyPattern = /^Bip01_(?:Pelvis|Spine\\d*|Neck|Head|[LR]_(?:Thigh|Calf|Foot|Toe\\d*|Clavicle|UpperArm|Forearm|Hand))$/;
          const bodyJointPeaks = ranked.filter(item => bodyPattern.test(item.bone)).slice(0, 20);
          output.push({
            exercise: clip.name,
            duration: clip.duration,
            sampleHz: hz,
            highestJointPeaks: ranked.slice(0, 20),
            bodyJointPeaks
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
      servedAssets: diagnostics.served,
      exercises: report
    }, null, 2));
    console.log('COACH_DIAGNOSTICS_OK', JSON.stringify({
      assetsServed: diagnostics.served.length,
      exercises: report.length,
      samples: report.length * 2
    }));
    for (const item of report.filter(x => x.exercise === 'jumpingjacks')) {
      console.log(JSON.stringify(item));
    }
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exit(1); });
