#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de notificación automática a Bing e IndexNow para coolpadelstudios.com.
Permite que Bing, Copilot, ChatGPT Search, Yandex y Seznam indexen instantáneamente
cualquier URL nueva o modificada tras cada despliegue.

Uso: python coolpadel-web/indexnow_ping.py [--dry-run]
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOST = "coolpadelstudios.com"
KEY = "10c2e37714e44c7082a97762c41e6914"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")


def extraer_urls_sitemap(sitemap_path: str, max_urls: int = 250) -> list[str]:
    """Extrae las URLs del sitemap.xml."""
    if not os.path.exists(sitemap_path):
        return [
            f"https://{HOST}/",
            f"https://{HOST}/camaras/",
            f"https://{HOST}/franquicias-padel/",
            f"https://{HOST}/blog/barometro-camaras-padel-2026/",
        ]

    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    urls = re.findall(r"<loc>(https://coolpadelstudios\.com/[^<]*)</loc>", content)
    # Priorizar URLs más relevantes si son más de max_urls
    return urls[:max_urls]


def notificar_indexnow(dry_run: bool = False):
    urls = extraer_urls_sitemap(SITEMAP_FILE)
    print(f"📡 Preparando ping a IndexNow con {len(urls)} URLs de {HOST}...")

    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }

    if dry_run:
        print("🔍 Modo --dry-run activado. No se envían peticiones HTTP.")
        print(f"   Key Location: {KEY_LOCATION}")
        print(f"   Primeras 5 URLs: {urls[:5]}")
        return

    json_data = json.dumps(payload).encode("utf-8")

    for endpoint in ENDPOINTS:
        try:
            req = urllib.request.Request(
                endpoint,
                data=json_data,
                headers={"Content-Type": "application/json; charset=utf-8"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                status = resp.status
                print(f"✅ Notificado {endpoint} -> Código HTTP: {status} (Indexación encolada)")
        except urllib.error.HTTPError as e:
            # Códigos 200 y 202 indican éxito en el protocolo IndexNow
            if e.code in (200, 202):
                print(f"✅ Notificado {endpoint} -> Código HTTP: {e.code} (Indexación encolada)")
            else:
                print(f"⚠️ Aviso en {endpoint} -> HTTP {e.code}: {e.reason}")
        except Exception as ex:
            print(f"⚠️ Error conectando con {endpoint}: {ex}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notificación a IndexNow (Bing, Copilot, ChatGPT Search)")
    parser.add_argument("--dry-run", action="store_true", help="Simular sin enviar la petición HTTP")
    args = parser.parse_args()
    notificar_indexnow(dry_run=args.dry_run)
