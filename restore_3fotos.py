#!/usr/bin/env python3
"""
Script de restauración inmediata a la versión de 3 fotos (coverflow rotativo).
Ejecuta: python coolpadel-web/restore_3fotos.py
"""
import shutil
import subprocess
import sys
import os

def restore():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    backup_file = os.path.join(base_dir, "build_multilingual_mobile_3fotos_backup.py")
    target_file = os.path.join(base_dir, "build_multilingual_mobile.py")

    if not os.path.exists(backup_file):
        print(f"❌ No se encontró el archivo de respaldo: {backup_file}")
        sys.exit(1)

    print("🔄 Restaurando versión de 3 fotos rotativas...")
    shutil.copyfile(backup_file, target_file)
    print("✅ Archivo build_multilingual_mobile.py restaurado.")

    print("🏗️ Reconstruyendo páginas web...")
    subprocess.run([sys.executable, target_file], cwd=os.path.dirname(base_dir), check=True)
    print("🎉 Versión de 3 fotos restaurada y compilada correctamente.")

if __name__ == "__main__":
    restore()
