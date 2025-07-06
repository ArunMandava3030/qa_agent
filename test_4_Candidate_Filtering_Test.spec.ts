import { test, expect } from '@playwright/test';

test('Test candidate filtering functionality', async ({ page }) => {
        await page.goto('https://recruiter.ai/candidates');
    await page.click('#filter-dropdown');
    await page.selectOption('#experience-filter', '3-5 years');
    await page.click('#apply-filter');
    await expect(page.locator('.filtered-results')).toBeVisible();
});
