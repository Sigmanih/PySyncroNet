"""
Configurazioni e costanti dell'applicazione
"""

DEFAULT_EXCLUSIONS = {
    'dirs': {
        'venv', '.venv', '__pycache__', '.git', '.vscode', '.idea',
        'node_modules', 'build', 'dist', 'models2', '.continue',
        '.vs', 'target', 'out', 'bin', 'obj', 'packages', '.gradle',
        '.settings', '.metadata', '.recommenders', 'gradle', 'jvm'
    },
    'files': {
        'config.py', 'settings.py', 'local_settings.py', '.env',
        '.gitignore', '.gitattributes', '.env.local', '.env.production',
        'package-lock.json', 'yarn.lock', 'thumbs.db', '.DS_Store',
        'desktop.ini', '*tmp', '*temp'
    },
    'extensions': {
        '.pyc', '.pyo', '.pyd', '.so', '.dll', '.exe', '.safetensors',
        '.bin', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp',
        '.ico', '.svg', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt',
        '.pptx', '.zip', '.rar', '.7z', '.tar', '.gz', '.mp4', '.avi',
        '.mkv', '.mov', '.mp3', '.wav', '.flac', '.ogg', '.db', '.sqlite',
        '.sqlite3', '.mdb', '.accdb', '.pdb', '.idb', '.class', '.jar',
        '.war', '.ear', '.metadata'
    }
}

APP_CONFIG = {
    'name': 'SyncroNet - Advanced PDF Project Manager',
    'version': '3.0',
    'author': 'Sigmanih',
    'repository': 'https://github.com/Sigmanih/PySyncroNet'
}

SUPPORTED_ENCODINGS = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
MAX_LINE_WIDTH = 100