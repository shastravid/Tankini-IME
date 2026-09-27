const { chromium } = require('playwright');
const path = require('path');

(async () => {
    console.log('Launching browser...');
    const browser = await chromium.launch({
        executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        headless: true
    });
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

    page.on('console', msg => {
        if (msg.type() === 'error') {
            console.error('Browser console error:', msg.text());
        }
    });

    console.log('Navigating to test suite...');
    await page.goto('http://localhost:8765/tests/index.html', { waitUntil: 'networkidle' });

    // Wait for keyboard loaded
    console.log('Waiting for KeymanWeb keyboard to initialize...');
    await page.waitForFunction(() => {
        const el = document.getElementById('status');
        return el && el.innerText.includes('Keyboard loaded');
    }, { timeout: 15000 });

    console.log('Keyboard loaded! Starting test suite...');
    page.on('requestfailed', req => console.log('Request failed:', req.url()));
    await page.evaluate(() => window.runAllTests());

    // Wait for completion
    console.log('Waiting for tests to complete...');
    await page.waitForFunction(() => {
        const el = document.getElementById('status');
        return el && el.innerText.includes('Complete');
    }, { timeout: 180000 });

    const status = await page.$eval('#status', el => el.innerText);
    console.log('\nStatus:', status);

    const summary = await page.$eval('#summary', el => el.innerText.replace(/\n+/g, ' | '));
    console.log('Summary:', summary);

    const failedTests = await page.evaluate(() => window.failedTests || []);
    console.log(`\nFailed tests count: ${failedTests.length}`);
    if (failedTests.length > 0) {
        console.log('Failed tests detail:');
        failedTests.forEach((f, idx) => {
            console.log(`  ${idx + 1}. [${f.desc}] Input: "${f.seq}" | Expected: "${f.expect}"`);
        });
    } else {
        console.log('🎉 ALL TESTS PASSED! 100% SUCCESS RATE!');
    }

    // Capture screenshot
    const screenshotPath = '/Users/shastravid/.gemini/antigravity-ide/brain/8d4ea19c-e532-44d2-9b02-7bdb2a68ca46/automated_test_results.png';
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`Screenshot saved to: ${screenshotPath}`);

    await browser.close();
    process.exit(failedTests.length > 0 ? 1 : 0);
})().catch(err => {
    console.error('Fatal error during test run:', err);
    process.exit(2);
});
