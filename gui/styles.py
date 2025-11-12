"""
Configurazione degli stili per l'interfaccia grafica
"""

import tkinter as tk
from tkinter import ttk

def setup_styles():
    """Configura gli stili per l'interfaccia con tema moderno"""
    style = ttk.Style()
    
    # Usa il tema 'clam' come base
    style.theme_use('clam')
    
    # Colori del tema
    bg_color = '#1e1e1e'
    fg_color = '#ffffff'
    accent_color = '#569cd6'
    success_color = '#388a34'
    warning_color = '#ce9178'
    text_color = '#d4d4d4'
    entry_bg = '#3c3c3c'
    border_color = '#444444'
    
    # Stili personalizzati
    style.configure('Custom.TFrame', background=bg_color)
    style.configure('Custom.TLabel', background=bg_color, foreground=fg_color)
    
    style.configure('Custom.TButton',
                   background='#0e639c',
                   foreground=fg_color,
                   focuscolor='none',
                   borderwidth=1,
                   relief='flat')
    
    style.configure('Success.TButton',
                   background=success_color,
                   foreground=fg_color,
                   font=('Segoe UI', 9, 'bold'))
    
    style.configure('Section.TLabelframe',
                   background=bg_color,
                   foreground=warning_color,
                   bordercolor=border_color,
                   relief='solid',
                   borderwidth=1)
    
    style.configure('Section.TLabelframe.Label',
                   background=bg_color,
                   foreground=warning_color)
    
    # Stile per la progress bar
    style.configure('Custom.Horizontal.TProgressbar',
                   background=accent_color,
                   troughcolor=entry_bg,
                   bordercolor=bg_color,
                   lightcolor=accent_color,
                   darkcolor=accent_color)
    
    # Stile per il notebook
    style.configure('TNotebook',
                   background=bg_color,
                   borderwidth=0)
    
    style.configure('TNotebook.Tab',
                   background='#2d2d30',
                   foreground=text_color,
                   padding=[15, 5],
                   focuscolor=bg_color)
    
    style.map('TNotebook.Tab',
             background=[('selected', bg_color),
                        ('active', '#3e3e42')],
             foreground=[('selected', accent_color),
                        ('active', fg_color)])