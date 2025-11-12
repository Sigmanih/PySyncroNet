"""
Utility per operazioni sul file system
"""

import os
import shutil
from pathlib import Path

def ensure_directory(path):
    """Assicura che una directory esista, creandola se necessario"""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path

def safe_file_write(file_path, content, encoding='utf-8'):
    """Scrive contenuto in un file in modo sicuro"""
    try:
        ensure_directory(Path(file_path).parent)
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Errore nella scrittura del file {file_path}: {e}")
        return False

def get_file_size(file_path):
    """Restituisce la dimensione di un file in MB"""
    try:
        size_bytes = os.path.getsize(file_path)
        return size_bytes / (1024 * 1024)  # Converti in MB
    except:
        return 0

def count_files_in_directory(directory, extensions=None):
    """Conta i file in una directory, opzionalmente filtrando per estensione"""
    directory = Path(directory)
    count = 0
    
    for file_path in directory.rglob('*'):
        if file_path.is_file():
            if extensions is None or file_path.suffix.lower() in extensions:
                count += 1
    
    return count

def clean_directory(directory, confirm=True):
    """Pulisce una directory (rimuove tutti i file e sottodirectory)"""
    directory = Path(directory)
    
    if not directory.exists():
        return True
    
    if confirm:
        # Qui potresti aggiungere una conferma
        pass
    
    try:
        for item in directory.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
        return True
    except Exception as e:
        print(f"Errore nella pulizia della directory {directory}: {e}")
        return False