#!/usr/bin/env python3
"""
Build script per PySyncroNet - Advanced PDF Project Manager
Crea un eseguibile standalone usando PyInstaller
"""

import os
import sys
import shutil
import platform
from pathlib import Path
import subprocess
from datetime import datetime

def setup_environment():
    """Configura l'ambiente di build"""
    print("🔧 Configurazione ambiente di build...")
    
    # Crea directory per i build artifacts
    build_dir = Path("build")
    release_dir = Path("release")
    
    # Pulisci build precedenti
    if build_dir.exists():
        shutil.rmtree(build_dir)
    if release_dir.exists():
        shutil.rmtree(release_dir)
    
    build_dir.mkdir(exist_ok=True)
    release_dir.mkdir(exist_ok=True)
    
    return build_dir, release_dir

def install_dependencies():
    """Installa le dipendenze necessarie"""
    print("📦 Installazione dipendenze...")
    
    requirements = [
        "fpdf>=1.7.2",
        "PyPDF2>=3.0.0",
        "pillow>=9.0.0"  # Per la gestione delle immagini nell'interfaccia
    ]
    
    for package in requirements:
        try:
            # Rimuovi le condizioni dalla stringa del pacchetto
            clean_package = package.split(';')[0].strip()
            subprocess.check_call([sys.executable, "-m", "pip", "install", clean_package])
            print(f"✅ {clean_package} installato")
        except subprocess.CalledProcessError as e:
            print(f"❌ Errore nell'installazione di {package}: {e}")
            return False
    
    return True

def create_spec_file(release_dir):
    """Crea il file .spec per PyInstaller con output diretto in release"""
    print("📄 Creazione file .spec...")
    
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

block_cipher = None

# Aggiungi il percorso corrente al PYTHONPATH
sys.path.append('.')

# Prepara i dati da includere
datas = []

# Includi la cartella saved se esiste
saved_path = Path('saved')
if saved_path.exists():
    for file in saved_path.glob('*'):
        if file.is_file():
            datas.append((str(file), 'saved'))

# Includi la cartella assets se esiste
assets_path = Path('assets')
if assets_path.exists():
    for file in assets_path.glob('*'):
        if file.is_file():
            datas.append((str(file), 'assets'))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'PIL',
        'PIL._tkinter_finder',
        'fpdf',
        'PyPDF2',
        'pathlib',
        'os',
        're',
        'threading',
        'datetime',
        'webbrowser',
        'subprocess',
        'shutil',
        'platform'
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Configurazione per eseguibile
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PySyncroNet',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico' if Path('assets/icon.ico').exists() else None,
)
'''
    
    with open('PySyncroNet.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ File .spec creato")

def build_executable(release_dir):
    """Esegue la build con PyInstaller"""
    print("🚀 Avvio build con PyInstaller...")
    
    try:
        # Usa il file .spec per la build con output diretto in release
        subprocess.check_call([
            sys.executable, 
            "-m", 
            "PyInstaller", 
            "PySyncroNet.spec",
            "--distpath", str(release_dir),  # Output diretto in release
            "--workpath", "build",
            "--clean",
            "--noconfirm"
        ])
        
        print("✅ Build completata con successo!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Errore durante la build: {e}")
        return False

def post_build_cleanup(release_dir):
    """Operazioni di pulizia post-build"""
    print("🧹 Pulizia post-build...")
    
    # Verifica che l'eseguibile sia stato creato
    exe_name = "PySyncroNet.exe" if platform.system() == "Windows" else "PySyncroNet"
    exe_path = release_dir / exe_name
    
    if exe_path.exists():
        print(f"✅ Eseguibile creato: {exe_path}")
        
        # Copia la cartella saved se esiste
        saved_src = Path("saved")
        saved_dest = release_dir / "saved"
        if saved_src.exists():
            if saved_dest.exists():
                shutil.rmtree(saved_dest)
            shutil.copytree(saved_src, saved_dest)
            print("✅ Cartella 'saved' copiata")
        
        # Copia la cartella assets se esiste
        assets_src = Path("assets")
        assets_dest = release_dir / "assets"
        if assets_src.exists():
            if assets_dest.exists():
                shutil.rmtree(assets_dest)
            shutil.copytree(assets_src, assets_dest)
            print("✅ Cartella 'assets' copiata")
        
        # Crea un README per la release
        readme_content = f"""PySyncroNet - Advanced PDF Project Manager
Versione: 3.1 (AI-Enhanced Edition)

Eseguibile standalone creato il: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ISTRUZIONI:
1. Esegui {exe_name} per avviare l'applicazione
2. Assicurati che le cartelle 'saved' e 'assets' siano nella stessa directory dell'eseguibile
3. L'applicazione creerà automaticamente i PDF nella cartella 'saved'

CARATTERISTICHE:
- Conversione progetti in PDF
- Ricostruzione progetti da PDF
- Gestione esclusioni avanzata
- Interfaccia grafica moderna

Sistema: {platform.system()} {platform.release()}
Python: {platform.python_version()}
"""
        
        with open(release_dir / "README.txt", "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print("✅ README creato")
        
    else:
        print("❌ Eseguibile non trovato!")
        return False
    
    # Rimuovi file temporanei
    temp_files = [
        "PySyncroNet.spec",
        "build",
    ]
    
    for file in temp_files:
        if Path(file).exists():
            if Path(file).is_dir():
                shutil.rmtree(file)
                print(f"✅ Cartella '{file}' rimossa")
            else:
                Path(file).unlink()
                print(f"✅ File '{file}' rimosso")
    
    return True

def verify_resources():
    """Verifica che le risorse necessarie esistano"""
    print("🔍 Verifica risorse...")
    
    required_resources = [
        Path("saved/syncronet_logo.png"),
        Path("main.py"),
    ]
    
    missing = []
    for resource in required_resources:
        if not resource.exists():
            missing.append(str(resource))
    
    if missing:
        print("❌ Risorse mancanti:")
        for item in missing:
            print(f"   - {item}")
        return False
    
    print("✅ Tutte le risorse principali trovate")
    
    # Crea assets se non esiste
    assets_dir = Path("assets")
    if not assets_dir.exists():
        assets_dir.mkdir()
        print("📁 Cartella assets creata")
    
    return True

def main():
    """Funzione principale"""
    print("🏗️  Build di PySyncroNet - Advanced PDF Project Manager")
    print("=" * 60)
    
    # Verifica che PyInstaller sia installato
    try:
        import PyInstaller
        print("✅ PyInstaller trovato")
    except ImportError:
        print("❌ PyInstaller non installato. Installalo con:")
        print("pip install pyinstaller")
        sys.exit(1)
    
    # Verifica risorse
    if not verify_resources():
        print("❌ Risorse mancanti, impossibile procedere con la build")
        sys.exit(1)
    
    # Setup ambiente
    build_dir, release_dir = setup_environment()
    
    # Installa dipendenze
    if not install_dependencies():
        print("❌ Errore nell'installazione delle dipendenze")
        sys.exit(1)
    
    # Crea file .spec
    create_spec_file(release_dir)
    
    # Esegui build
    if not build_executable(release_dir):
        print("❌ Build fallita")
        sys.exit(1)
    
    # Pulizia post-build
    if not post_build_cleanup(release_dir):
        print("❌ Errore nella pulizia post-build")
        sys.exit(1)
    
    print("🎉 Build completata con successo!")
    print("📁 L'eseguibile si trova nella cartella 'release'")
    print("\n📋 Contenuto della release:")
    for item in release_dir.iterdir():
        if item.is_file():
            print(f"   📄 {item.name}")
        else:
            print(f"   📁 {item.name}/")
    
    print("\n💡 Note importanti:")
    print("   - L'eseguibile è pronto per l'uso")
    print("   - Tutte le risorse sono incluse nella cartella 'release'")
    print("   - Puoi spostare la cartella 'release' ovunque tu voglia")

if __name__ == "__main__":
    main()