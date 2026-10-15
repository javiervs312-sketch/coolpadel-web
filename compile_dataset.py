# -*- coding: utf-8 -*-
"""
compile_dataset.py
Ensambla todas las listas modulares en coolpadel-web/dataset_franquicias.py.
"""
import os
import json

from generate_dataset import DATASET as UK_LIST
from make_master_dataset import ES_LIST
from dataset_rest_europe import FR_LIST, IT_LIST, BE_NL_LIST, DACH_LIST, NORDIC_LIST, PT_LIST
from dataset_rest_world import US_LIST, LATAM_LIST, ME_LIST, ZA_AU_LIST
from dataset_scraper_new import (
    NEW_UK_LIST, NEW_NORDIC_LIST, NEW_DACH_LIST, NEW_BENELUX_LIST,
    NEW_PT_LIST, NEW_LATAM_LIST, NEW_WORLD_LIST
)

# Agrupaciones completas
FINAL_UK = UK_LIST + NEW_UK_LIST
FINAL_ES = ES_LIST
FINAL_FR = FR_LIST
FINAL_IT = IT_LIST
FINAL_BE_NL = BE_NL_LIST + NEW_BENELUX_LIST
FINAL_DACH = DACH_LIST + NEW_DACH_LIST + [x for x in NEW_WORLD_LIST if x.get("region_filtro") == "DE"]
FINAL_NORDIC = NORDIC_LIST + NEW_NORDIC_LIST
FINAL_PT = PT_LIST + NEW_PT_LIST
FINAL_US = US_LIST
FINAL_LATAM = LATAM_LIST + NEW_LATAM_LIST
FINAL_ME = ME_LIST
FINAL_ZA_AU = ZA_AU_LIST + [x for x in NEW_WORLD_LIST if x.get("region_filtro") == "ZA"]

ALL_OPERATORS = (
    FINAL_UK +
    FINAL_ES +
    FINAL_FR +
    FINAL_IT +
    FINAL_BE_NL +
    FINAL_DACH +
    FINAL_NORDIC +
    FINAL_PT +
    FINAL_US +
    FINAL_LATAM +
    FINAL_ME +
    FINAL_ZA_AU
)

def main():
    target_path = os.path.join(os.path.dirname(__file__), "dataset_franquicias.py")
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write(f'"""\nBase de datos de {len(ALL_OPERATORS)} cadenas multiclub (+1 club abierto bajo la misma marca) y franquicias de pádel a nivel mundial.\n"""\n\n')
        f.write(f"# Total de entidades: {len(ALL_OPERATORS)}\n")
        f.write("FRANQUICIAS = " + json.dumps(ALL_OPERATORS, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] dataset_franquicias.py generado con exito en: {target_path}")
    print(f"[TOTAL] Total de cadenas y franquicias: {len(ALL_OPERATORS)}")
    print("\nDesglose por region:")
    print(f"  GB Reino Unido e Irlanda: {len(FINAL_UK)}")
    print(f"  ES Espana: {len(FINAL_ES)}")
    print(f"  FR Francia: {len(FINAL_FR)}")
    print(f"  IT Italia: {len(FINAL_IT)}")
    print(f"  NL Benelux: {len(FINAL_BE_NL)}")
    print(f"  DE DACH (Alemania, AT, CH): {len(FINAL_DACH)}")
    print(f"  SE Nordicos (Suecia, NO, DK, FI): {len(FINAL_NORDIC)}")
    print(f"  PT Portugal: {len(FINAL_PT)}")
    print(f"  US Estados Unidos: {len(FINAL_US)}")
    print(f"  MX Latinoamerica (Mexico, Chile, AR, BR): {len(FINAL_LATAM)}")
    print(f"  AE Oriente Medio (EAU, Catar, Kuwait): {len(FINAL_ME)}")
    print(f"  ZA Sudafrica & Australia: {len(FINAL_ZA_AU)}")

if __name__ == "__main__":
    main()
