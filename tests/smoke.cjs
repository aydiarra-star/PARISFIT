// Run against a local HTTP server; requires @playwright/test and Chromium.
// BASE_URL=http://localhost:3000 node tests/smoke.cjs
const assert = require('node:assert/strict');
const { chromium } = require('@playwright/test');
(async () => {
  const browser = await chromium.launch({headless:true, ...(process.env.CHROMIUM_PATH ? {executablePath:process.env.CHROMIUM_PATH,args:['--no-sandbox','--disable-dev-shm-usage']} : {})});
  try {
    const context = await browser.newContext();
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(process.env.BASE_URL || 'http://localhost:3000');
    for (const width of [320, 375, 390, 720, 900, 1440]) {
      await page.setViewportSize({width,height:900});
      assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `Overflow at ${width}px`);
      assert.equal(await page.locator('#view-today .essentials button').count(), 4);
    }
    await page.setViewportSize({width:390,height:844});
    await page.locator('#water-quick').click();
    assert.equal(await page.locator('#water-percent').textContent(), '13%');
    await page.reload();
    assert.equal(await page.locator('#water-percent').textContent(), '13%');
    await page.locator('[data-energy]').first().click();
    await page.locator('[data-e="low"]').click();
    assert.equal(await page.locator('#energy').textContent(), 'Douce');
    await page.locator('#read-discipline').click();
    assert.equal(await page.locator('#modal li').count(), 5);
    await page.locator('.close').click();
    await page.locator('#challenges').click();
    await page.locator('#challenge-add').click();
    await page.locator('#habit-save').click();
    await page.locator('.mobile-nav [data-view="switch"]').click();
    assert.match(await page.locator('#habits').textContent(), /10 minutes de scroll/);
    await page.locator('.mobile-nav [data-view="today"]').click();
    await page.locator('#workout-rec').click();
    assert(await page.locator('#view-coach').isVisible());
    await page.evaluate(() => navigator.serviceWorker.ready);
    await page.reload();
    await context.setOffline(true);
    await page.reload();
    assert(await page.locator('#view-today').isVisible());
    assert(await page.locator('.hero-art img').evaluate(img => img.complete && img.naturalWidth > 0));
    assert.equal(await page.locator('#energy').textContent(), 'Douce');
    assert.deepEqual(errors, []);
    console.log('PASS: responsive widths, hydration persistence, energy, reading, challenge, coach, offline cache.');
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode=1; });
