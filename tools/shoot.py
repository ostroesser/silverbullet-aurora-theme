import sys, asyncio
from playwright.async_api import async_playwright
BASE = "http://127.0.0.1:3111"
out = sys.argv[1]
STYLED = "[...document.querySelectorAll('style')].some(s=>s.textContent.includes('--au-bg'))"

async def go(page, path, theme):
    await page.goto(BASE + path)
    await page.wait_for_selector(".cm-content", timeout=60000)
    try: await page.wait_for_function(STYLED, timeout=30000)
    except Exception: print("WARN: style not injected on", path)
    await page.evaluate(f"document.documentElement.dataset.theme='{theme}'")
    await page.evaluate("document.fonts.ready")
    await page.wait_for_timeout(1500)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={"width": 1400, "height": 1500}, device_scale_factor=1)
        page = await ctx.new_page()
        for theme in ["light", "dark"]:
            await page.emulate_media(color_scheme=theme)
            await go(page, "/index", theme)
            await page.screenshot(path=f"{out}-{theme}-index.png")
            await page.set_viewport_size({"width": 1400, "height": 800})
            await go(page, "/Projects/Atlas", theme)
            await page.screenshot(path=f"{out}-{theme}-atlas.png")
            await page.keyboard.press("Control+k"); await page.wait_for_timeout(1200)
            await page.screenshot(path=f"{out}-{theme}-picker.png")
            await page.keyboard.press("Escape")
            # mobile
            await page.set_viewport_size({"width": 400, "height": 860})
            await go(page, "/index", theme)
            await page.screenshot(path=f"{out}-{theme}-mobile.png")
            await page.set_viewport_size({"width": 1400, "height": 1500})
        await b.close()
asyncio.run(main())
