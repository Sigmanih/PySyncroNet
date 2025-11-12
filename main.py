#!/usr/bin/env python3
"""
PySyncroNet - Advanced PDF Project Manager
Punto di ingresso principale dell'applicazione
"""

import tkinter as tk
from gui.main_window import MainWindow

def main():
    """Avvia l'applicazione principale"""
    try:
        root = tk.Tk()
        app = MainWindow(root)
        root.mainloop()
    except Exception as e:
        print(f"Errore nell'avvio dell'applicazione: {e}")
        raise

if __name__ == "__main__":
    main()