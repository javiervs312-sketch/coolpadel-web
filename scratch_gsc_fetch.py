# -*- coding: utf-8 -*-
"""Script temporal para extraer datos de Google Search Console."""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

# Cargar credenciales
creds_data = json.load(open("../comun/token_gsc.json"))
cred_app = json.load(open("../credentials.json"))["installed"]

creds = Credentials(
    token=creds_data["access_token"],
    refresh_token=creds_data["refresh_token"],
    token_uri="https://oauth2.googleapis.com/token",
    client_id=cred_app["client_id"],
    client_secret=cred_app["client_secret"],
    scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
)

# Refrescar si está caducado
if creds.expired:
    creds.refresh(Request())

service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
site_url = "https://coolpadelstudios.com/"
start_date = "2026-08-16"
end_date = "2026-11-14"

def query_gsc(dimensions, row_limit=50, filters=None):
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions,
        "rowLimit": row_limit
    }
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=site_url, body=body).execute()

results = {}

print("=== TOP 50 QUERIES ===")
r = query_gsc(["query"], 50)
results["queries"] = r.get("rows", [])
for row in results["queries"][:20]:
    print(f"  {row['keys'][0][:60]:<60} clics={row['clicks']} imp={row['impressions']} ctr={row['ctr']:.2%} pos={row['position']:.1f}")

print("\n=== TOP 30 PÁGINAS ===")
r = query_gsc(["page"], 30)
results["pages"] = r.get("rows", [])
for row in results["pages"][:20]:
    print(f"  {row['keys'][0][:70]:<70} clics={row['clicks']} imp={row['impressions']} ctr={row['ctr']:.2%} pos={row['position']:.1f}")

print("\n=== RENDIMIENTO POR PAÍS ===")
r = query_gsc(["country"], 50)
results["countries"] = r.get("rows", [])
for row in results["countries"][:25]:
    print(f"  {row['keys'][0]:<10} clics={row['clicks']} imp={row['impressions']} ctr={row['ctr']:.2%} pos={row['position']:.1f}")

# Guardar resultados completos
with open("../scratch_gsc_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nTotal queries: {len(results['queries'])}")
print(f"Total pages: {len(results['pages'])}")
print(f"Total countries: {len(results['countries'])}")
print("Guardado en scratch_gsc_results.json")
