"""
Modulo per la gestione dei file e sistema di esclusioni
"""

import os
from pathlib import Path
from core.config import DEFAULT_EXCLUSIONS

class FileManager:
    """Gestisce le operazioni sui file e il sistema di esclusioni"""
    
    def __init__(self):
        self.excluded_dirs = set(DEFAULT_EXCLUSIONS['dirs'])
        self.excluded_files = set(DEFAULT_EXCLUSIONS['files'])
        self.excluded_extensions = set(DEFAULT_EXCLUSIONS['extensions'])
    
    def should_exclude(self, file_path, relative_path):
        """Determina se un file/cartella dovrebbe essere escluso"""
        relative_path_str = str(relative_path)
        
        # Controlla se è in una cartella esclusa
        if any(excluded_dir in relative_path_str.split(os.sep) 
               for excluded_dir in self.excluded_dirs):
            return True
        
        # Controlla se è un file escluso
        if file_path.name in self.excluded_files:
            return True
        
        # Controlla se l'estensione è esclusa
        if file_path.suffix.lower() in self.excluded_extensions:
            return True
        
        # Controlla pattern con wildcard
        for pattern in self.excluded_files:
            if '*' in pattern:
                import fnmatch
                if fnmatch.fnmatch(file_path.name, pattern):
                    return True
        
        return False
    
    def count_project_files(self, project_path):
        """Conta i file nel progetto considerando le esclusioni"""
        project_path = Path(project_path)
        count = 0
        
        for file_path in project_path.rglob('*'):
            if file_path.is_file():
                try:
                    relative_path = file_path.relative_to(project_path)
                    if not self.should_exclude(file_path, relative_path):
                        count += 1
                except ValueError:
                    continue
        
        return count
    
    def get_project_stats(self, project_path):
        """Restituisce statistiche del progetto"""
        project_path = Path(project_path)
        total_files = 0
        total_size = 0
        extensions = {}
        
        for file_path in project_path.rglob('*'):
            if file_path.is_file():
                total_files += 1
                total_size += file_path.stat().st_size
                ext = file_path.suffix.lower()
                extensions[ext] = extensions.get(ext, 0) + 1
        
        return {
            'total_files': total_files,
            'total_size_mb': total_size / (1024 * 1024),
            'extensions': extensions
        }
    
    def update_exclusions(self, dirs=None, files=None, extensions=None):
        """Aggiorna le esclusioni"""
        if dirs is not None:
            self.excluded_dirs = set(dirs)
        if files is not None:
            self.excluded_files = set(files)
        if extensions is not None:
            self.excluded_extensions = set(extensions)
    
    def get_exclusions(self):
        """Restituisce le esclusioni correnti"""
        return {
            'dirs': sorted(self.excluded_dirs),
            'files': sorted(self.excluded_files),
            'extensions': sorted(self.excluded_extensions)
        }