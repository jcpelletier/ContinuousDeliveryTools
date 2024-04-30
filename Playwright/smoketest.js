const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({
        headless: true // Set to false to see the browser UI
    });
    const page = await browser.newPage();
    await page.goto('https://www.google.com/');
    await page.screenshot({ path: `build/example.png` });
    await browser.close();
})();