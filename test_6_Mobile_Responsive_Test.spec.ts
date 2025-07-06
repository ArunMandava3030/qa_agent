import { test, expect } from '@playwright/test';

test('Test mobile responsiveness', async ({ page }) => {
        await page.setViewportSize({ width: 375, height: 667 });
    await page.goto('https://recruiter.ai');
    await expect(page.locator('.mobile-menu')).toBeVisible();
    await page.click('.mobile-menu-toggle');
    await expect(page.locator('.mobile-nav')).toBeVisible();
});
