"""
Sistema di logging per l'applicazione
"""

import logging
import os
from datetime import datetime
from pathlib import Path

def setup_logger(name='PySyncroNet', log_level=logging.INFO):
    """Configura e restituisce un logger"""
    # Crea la directory dei log se non esiste
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    # Nome file log con timestamp
    log_file = log_dir / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    # Configura il logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Formattatore
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler per file
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Handler per console (opzionale)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

class GUILogger:
    """Logger specializzato per l'interfaccia grafica"""
    
    def __init__(self, text_widget=None):
        self.text_widget = text_widget
        self.logger = setup_logger('PySyncroNet_GUI')
    
    def log(self, message, level='info'):
        """Logga un messaggio"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted_message = f"{timestamp} - {message}"
        
        # Log nel file
        if level == 'error':
            self.logger.error(message)
        elif level == 'warning':
            self.logger.warning(message)
        else:
            self.logger.info(message)
        
        # Log nell'interfaccia se disponibile
        if self.text_widget:
            self.text_widget.insert(tk.END, f"{formatted_message}\n")
            self.text_widget.see(tk.END)
            self.text_widget.update_idletasks()
    
    def info(self, message):
        """Logga un messaggio informativo"""
        self.log(message, 'info')
    
    def error(self, message):
        """Logga un messaggio di errore"""
        self.log(message, 'error')
    
    def warning(self, message):
        """Logga un messaggio di warning"""
        self.log(message, 'warning')