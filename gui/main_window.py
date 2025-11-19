"""
Finestra principale dell'applicazione
"""

import tkinter as tk
from tkinter import ttk
from gui.tabs.pdf_creator_tab import PDFCreatorTab
from gui.tabs.project_recreator_tab import ProjectRecreatorTab
from gui.tabs.exclusions_tab import ExclusionsTab
from gui.tabs.settings_tab import SettingsTab
from gui.styles import setup_styles
from core.config import APP_CONFIG
from PIL import Image, ImageTk, ImageDraw

class MainWindow:
    """Finestra principale dell'applicazione"""
    
    def __init__(self, root):
        self.root = root
        self._setup_window()
        self._create_widgets()
    
    def _setup_window(self):
        """Configura la finestra principale"""
        self.root.title(f"{APP_CONFIG['name']} v{APP_CONFIG['version']}")
        self.root.geometry("1100x850")
        self.root.configure(bg='#1e1e1e')
        self.root.minsize(1000, 1000)
        
        # Prova a impostare l'icona
        try:
            self.root.iconbitmap('assets/icon.ico')
        except:
            pass
        
        setup_styles()
    
    def _create_widgets(self):
        """Crea i widget dell'interfaccia"""
        self._create_header()
        self._create_notebook()
        self._create_status_bar()
    

    def _create_header(self):
        header_frame = tk.Frame(self.root, bg='#1e1e1e')
        header_frame.pack(fill='x', padx=20, pady=15)

        # Carica e ridimensiona il logo
        try:
            import sys
            import os
            from pathlib import Path
            
            # Determina il percorso base
            if getattr(sys, 'frozen', False):
                # Se l'app è eseguita come eseguibile PyInstaller
                base_path = Path(sys._MEIPASS)
            else:
                # Se eseguita come script Python
                base_path = Path(__file__).parent.parent
            
            # Prova diversi percorsi per il logo
            logo_paths = [
                base_path / 'saved' / 'syncronet_logo.png',  # Percorso in eseguibile
                Path('saved') / 'syncronet_logo.png',        # Percorso relativo
                Path(__file__).parent.parent / 'saved' / 'syncronet_logo.png',  # Percorso assoluto
            ]
            
            logo_loaded = False
            for logo_path in logo_paths:
                try:
                    if logo_path.exists():
                        img = Image.open(logo_path)
                        img = img.resize((96, 96), Image.LANCZOS)
                        self.logo_img = ImageTk.PhotoImage(img)
                        logo_loaded = True
                        print(f"✅ Logo caricato da: {logo_path}")
                        break
                except Exception as e:
                    print(f"❌ Errore nel caricamento del logo da {logo_path}: {e}")
                    continue
            
            if not logo_loaded:
                # Crea un'immagine placeholder
                print("⚠️  Logo non trovato, creo placeholder")
                img = Image.new('RGB', (96, 96), color='#1e1e1e')
                self.logo_img = ImageTk.PhotoImage(img)
                
        except Exception as e:
            print(f"❌ Errore critico nel caricamento del logo: {e}")
            # Fallback a placeholder
            img = Image.new('RGB', (96, 96), color='#1e1e1e')
            self.logo_img = ImageTk.PhotoImage(img)
        
        # Maschera circolare
        mask = Image.new("L", (96, 96), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 96, 96), fill=255)

        # Applica la maschera all'immagine
        img.putalpha(mask)

        # --- FRAME ORIZZONTALE: LOGO + TESTI ---
        main_row = tk.Frame(header_frame, bg='#1e1e1e')
        main_row.pack(anchor="center")

        # Converti per Tkinter
        self.logo_img = ImageTk.PhotoImage(img)

        # Logo a sinistra
        logo_label = tk.Label(main_row, image=self.logo_img, bg='#1e1e1e')
        logo_label.pack(side="left", padx=(0, 15))

        # --- SUB-HEADER A DESTRA DEL LOGO (TITOLO + SOTTOTITOLO) ---
        text_column = tk.Frame(main_row, bg='#1e1e1e')
        text_column.pack(side="left", anchor="w")

        # Titolo
        title_label = tk.Label(
            text_column,
            text="SyncroNet - Advanced PDF Project Manager",
            font=('Segoe UI', 22, 'bold'),
            bg='#1e1e1e',
            fg='#569cd6'
        )
        title_label.pack(anchor="w")

        # Sottotitolo
        subtitle_label = tk.Label(
            text_column,
            text="Converti progetti in PDF e ricostruisci progetti da PDF • Preservazione perfetta dell'indentazione",
            font=('Segoe UI', 11),
            bg='#1e1e1e',
            fg='#9cdcfe'
        )
        subtitle_label.pack(anchor="w", pady=(5, 0))

        # Separatore
        separator = ttk.Separator(self.root, orient='horizontal')
        separator.pack(fill='x', padx=20, pady=5)


    
    def _create_notebook(self):
        """Crea il notebook con le schede"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Crea le schede
        self.tabs = {
            'pdf_creator': PDFCreatorTab(self.notebook),
            'project_recreator': ProjectRecreatorTab(self.notebook),
            'exclusions': ExclusionsTab(self.notebook),
            'settings': SettingsTab(self.notebook)
        }
        
        # Aggiungi le schede al notebook
        self.notebook.add(self.tabs['pdf_creator'].frame, text=self.tabs['pdf_creator'].title)
        self.notebook.add(self.tabs['project_recreator'].frame, text=self.tabs['project_recreator'].title)
        self.notebook.add(self.tabs['exclusions'].frame, text=self.tabs['exclusions'].title)
        self.notebook.add(self.tabs['settings'].frame, text=self.tabs['settings'].title)
    
    def _create_status_bar(self):
        """Crea la status bar"""
        status_frame = tk.Frame(self.root, bg='#2d2d30', height=25)
        status_frame.pack(fill='x', side='bottom')
        status_frame.pack_propagate(False)
        
        # Status message
        self.status_var = tk.StringVar(value="✅ Pronto - Seleziona un'operazione per iniziare")
        status_label = tk.Label(
            status_frame,
            textvariable=self.status_var,
            font=('Segoe UI', 9),
            bg='#2d2d30',
            fg='#569cd6'
        )
        status_label.pack(side='left', padx=10, pady=3)
        
        # Versione
        version_label = tk.Label(
            status_frame,
            text=f"v{APP_CONFIG['version']} • SyncroNet",
            font=('Segoe UI', 8),
            bg='#2d2d30',
            fg='#858585'
        )
        version_label.pack(side='right', padx=10, pady=3)
    
    def update_status(self, message):
        """Aggiorna il messaggio di status"""
        from datetime import datetime
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.status_var.set(f"🕒 {timestamp} - {message}")
        self.root.update_idletasks()