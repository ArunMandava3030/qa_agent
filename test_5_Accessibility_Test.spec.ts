import { test, expect } from '@playwright/test';

test('Test accessibility features', async ({ page }) => {
        await page.goto('https://recruiter.ai');
    // Accessibility check - requires @axe-core/playwright
    // await injectAxe(page);
    // await checkA11y(page);
    await expect(page.locator('h1')).toHaveAttribute('aria-label');
});
