import json
with open('../scratch_gsc_results.json') as f:
    d = json.load(f)

print('=== QUERIES CON MAS IMPRESIONES (oportunidades) ===')
queries = sorted(d['queries'], key=lambda x: x['impressions'], reverse=True)
for r in queries[:30]:
    pos = r['position']
    imp = r['impressions']
    clics = r['clicks']
    ctr = r['ctr']*100
    kw = r['keys'][0][:60]
    print(f"  pos={pos:5.1f} imp={imp:5} clics={clics:3} ctr={ctr:5.1f}%  {kw}")

print()
print('=== PAGINAS CON MAS IMPRESIONES (oportunidades CTR) ===')
pages = sorted(d['pages'], key=lambda x: x['impressions'], reverse=True)
for r in pages[:20]:
    pos = r['position']
    imp = r['impressions']
    clics = r['clicks']
    ctr = r['ctr']*100
    url = r['keys'][0].replace('https://coolpadelstudios.com','')[:70]
    print(f"  pos={pos:5.1f} imp={imp:5} clics={clics:3} ctr={ctr:5.1f}%  {url}")

print()
print('=== TODOS LOS PAISES ===')
countries_sorted = sorted(d['countries'], key=lambda x: x['clicks'], reverse=True)
for r in countries_sorted:
    cc = r['keys'][0]
    clics = r['clicks']
    imp = r['impressions']
    ctr = r['ctr']*100
    pos = r['position']
    print(f"  {cc:<8} clics={clics:4} imp={imp:5} ctr={ctr:5.1f}% pos={pos:5.1f}")
