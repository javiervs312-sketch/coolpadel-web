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

ALL_OPERATORS = (
    UK_LIST +
    ES_LIST +
    FR_LIST +
    IT_LIST +
    BE_NL_LIST +
    DACH_LIST +
    NORDIC_LIST +
    PT_LIST +
    US_LIST +
    LATAM_LIST +
    ME_LIST +
    ZA_AU_LIST
)

def main():
    target_path = os.path.join(os.path.dirname(__file__), "dataset_franquicias.py")
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nBase de datos de 106 cadenas multiclub (+1 club abierto bajo la misma marca) y franquicias de pádel a nivel mundial.\n"""\n\n')
        f.write(f"# Total de entidades: {len(ALL_OPERATORS)}\n")
        f.write("FRANQUICIAS = " + json.dumps(ALL_OPERATORS, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] dataset_franquicias.py generado con exito en: {target_path}")
    print(f"[TOTAL] Total de cadenas y franquicias: {len(ALL_OPERATORS)}")
    print("\nDesglose por region:")
    print(f"  GB Reino Unido: {len(UK_LIST)}")
    print(f"  ES Espana: {len(ES_LIST)}")
    print(f"  FR Francia: {len(FR_LIST)}")
    print(f"  IT Italia: {len(IT_LIST)}")
    print(f"  NL Benelux: {len(BE_NL_LIST)}")
    print(f"  DE DACH (Alemania, AT, CH): {len(DACH_LIST)}")
    print(f"  SE Nordicos: {len(NORDIC_LIST)}")
    print(f"  PT Portugal: {len(PT_LIST)}")
    print(f"  US Estados Unidos: {len(US_LIST)}")
    print(f"  MX Latinoamerica: {len(LATAM_LIST)}")
    print(f"  AE Oriente Medio: {len(ME_LIST)}")
    print(f"  ZA Sudafrica & Australia: {len(ZA_AU_LIST)}")

if __name__ == "__main__":
    main()
