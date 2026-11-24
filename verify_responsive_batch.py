import asyncio
import os
import sys
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VIEWPORTS = [
    {"name": "mobile_small", "width": 360, "height": 640},
    {"name": "mobile_iphone", "width": 390, "height": 844},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "desktop", "width": 1280, "height": 800},
]

TEST_PAGES = [
    {"rel": "camaras/paraguay/asuncion/index.html", "variant": "B", "iso": "PY"},
    {"rel": "camaras/france/index.html", "variant": "B", "iso": "FR"},
    {"rel": "camaras/deutschland/index.html", "variant": "B", "iso": "DE"},
    {"rel": "camaras/japan/tokyo/index.html", "variant": "B", "iso": "JP"},
    {"rel": "camaras/united-kingdom/london/index.html", "variant": "B", "iso": "GB"},
    {"rel": "camaras/espana/index.html", "variant": "B", "iso": "ES"},
    {"rel": "camaras/mexico/index.html", "variant": "A", "iso": "MX"},
    {"rel": "camaras/united-states/index.html", "variant": "A", "iso": "US"},
]

async def run_audit():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        all_passed = True
        
        for item in TEST_PAGES:
            full_path = os.path.join(BASE_DIR, item["rel"])
            if not os.path.exists(full_path):
                print(f"[ERROR] Not found: {full_path}")
                all_passed = False
                continue
                
            page_url = f"file:///{full_path.replace(chr(92), '/')}"
            print(f"\n--- Probando: {item['rel']} (Variante {item['variant']}) ---")
            
            for vp in VIEWPORTS:
                context = await browser.new_context(viewport={"width": vp["width"], "height": vp["height"]})
                page = await context.new_page()
                await page.goto(page_url, wait_until="load")
                
                # Check horizontal overflow
                overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
                scroll_w = await page.evaluate("() => document.documentElement.scrollWidth")
                
                if overflow:
                    print(f"  [FALLO] {vp['name']} ({vp['width']}px): Overflow horizontal detectado! scrollWidth={scroll_w}")
                    all_passed = False
                else:
                    print(f"  [OK] {vp['name']} ({vp['width']}px): Sin overflow (scrollWidth={scroll_w})")
                    
                # If variant B on mobile, check centering of stat card and article card
                if item["variant"] == "B" and "mobile" in vp["name"]:
                    stat_card = page.locator(".hero-stat-card").first
                    if await stat_card.count() > 0:
                        box = await stat_card.bounding_box()
                        if box:
                            left = round(box['x'])
                            right = round(vp['width'] - (box['x'] + box['width']))
                            symmetric = abs(left - right) <= 2
                            print(f"    -> Stat card: left={left}px, width={round(box['width'])}px, right={right}px (Simétrico: {symmetric})")
                            if not symmetric:
                                all_passed = False
                                
                    article_card = page.locator(".article-card").first
                    if await article_card.count() > 0:
                        box_art = await article_card.bounding_box()
                        if box_art:
                            left_art = round(box_art['x'])
                            right_art = round(vp['width'] - (box_art['x'] + box_art['width']))
                            symmetric_art = abs(left_art - right_art) <= 2
                            print(f"    -> Article card: left={left_art}px, width={round(box_art['width'])}px, right={right_art}px (Simétrico: {symmetric_art})")
                            if not symmetric_art:
                                all_passed = False
                                
                await context.close()
                
        await browser.close()
        
        print("\n==========================================")
        if all_passed:
            print("TODAS LAS PRUEBAS RESPONSIVE Y DE CENTRADO PASARON EXITOSAMENTE!")
        else:
            print("ALGUNAS PRUEBAS FALLARON, REVISAR DETALLES ARRIBA.")
        print("==========================================")

if __name__ == '__main__':
    asyncio.run(run_audit())
