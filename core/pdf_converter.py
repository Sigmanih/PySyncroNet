"""
Modulo per la conversione di progetti in documenti PDF
"""

import os
from pathlib import Path
from fpdf import FPDF
from core.file_manager import FileManager
from core.config import SUPPORTED_ENCODINGS, MAX_LINE_WIDTH

class PDFConverter:
    """Gestisce la conversione di progetti in PDF"""
    
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.file_manager = FileManager()
    
    def create_project_pdf(self, project_path, output_pdf, custom_exclusions=None, progress_callback=None):
        """Crea un PDF dal progetto"""
        # Applica esclusioni personalizzate
        if custom_exclusions:
            self.file_manager.update_exclusions(**custom_exclusions)
        
        project_path = Path(project_path)
        
        if not project_path.exists():
            raise ValueError(f"La cartella '{project_path}' non esiste.")
        
        # Conta i file totali
        total_files = self.file_manager.count_project_files(project_path)
        processed_count = 0
        
        # Pagina titolo
        self._add_title_page(project_path)
        
        # Elenco file processati
        processed_files = []
        
        # Processa tutti i file
        for file_path in project_path.rglob('*'):
            if file_path.is_file():
                relative_path = file_path.relative_to(project_path)
                
                if not self.file_manager.should_exclude(file_path, relative_path):
                    self._add_file_to_pdf(file_path, relative_path)
                    processed_files.append(str(relative_path))
                    
                    # Aggiorna il progresso
                    processed_count += 1
                    if progress_callback:
                        progress_callback(processed_count, total_files)
        
        # Salva il PDF
        self.pdf.output(output_pdf)
        return len(processed_files)
    
    def _add_title_page(self, project_path):
        """Aggiunge la pagina titolo al PDF"""
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 20)
        self.pdf.cell(0, 20, "DOCUMENTAZIONE PROGETTO PYTHON", ln=True, align='C')
        self.pdf.ln(10)
        self.pdf.set_font('Arial', '', 12)
        self.pdf.cell(0, 10, f'Progetto: {project_path.name}', ln=True)
        self.pdf.cell(0, 10, f'Cartella: {project_path.absolute()}', ln=True)
        self.pdf.ln(10)
        
        # Aggiungi informazioni sulle esclusioni
        self._add_exclusions_info()
    
    def _add_exclusions_info(self):
        """Aggiunge informazioni sulle esclusioni al PDF"""
        exclusions = self.file_manager.get_exclusions()
        
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.cell(0, 10, "Cartelle escluse:", ln=True)
        self.pdf.set_font('Arial', '', 10)
        
        if exclusions['dirs']:
            for excluded_dir in exclusions['dirs']:
                self.pdf.cell(0, 5, f" - {excluded_dir}", ln=True)
        else:
            self.pdf.cell(0, 5, "Nessuna cartella esclusa", ln=True)
        
        self.pdf.ln(5)
        
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.cell(0, 10, "Estensioni escluse:", ln=True)
        self.pdf.set_font('Arial', '', 10)
        
        if exclusions['extensions']:
            for excluded_ext in exclusions['extensions']:
                self.pdf.cell(0, 5, f" - {excluded_ext}", ln=True)
        else:
            self.pdf.cell(0, 5, "Nessuna estensione esclusa", ln=True)
        
        self.pdf.ln(5)
        
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.cell(0, 10, "File esclusi:", ln=True)
        self.pdf.set_font('Arial', '', 10)
        
        if exclusions['files']:
            for excluded_file in exclusions['files']:
                self.pdf.cell(0, 5, f" - {excluded_file}", ln=True)
        else:
            self.pdf.cell(0, 5, "Nessun file escluso", ln=True)
        
        self.pdf.ln(10)
    
    def _add_file_to_pdf(self, file_path, relative_path):
        """Aggiunge un file al PDF"""
        try:
            # Leggi il contenuto del file
            content = self._read_file_content(file_path)
            
            # Pulisci il testo
            content = self._clean_text(content)
            relative_path_str = self._clean_text(str(relative_path))
            
            # Aggiungi una nuova pagina
            self.pdf.add_page()
            
            # Intestazione del file
            self.pdf.set_font('Arial', 'B', 14)
            self.pdf.cell(0, 10, f'File: {relative_path_str}', ln=True)
            self.pdf.ln(5)
            
            # Contenuto del file
            self.pdf.set_font('Courier', '', 8)
            
            # Dividi il contenuto in linee
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                clean_line = self._clean_text(line)
                
                if len(clean_line) <= MAX_LINE_WIDTH:
                    # Linea normale
                    line_number = f'{i:4d}|'
                    self.pdf.set_font('Courier', '', 8)
                    self.pdf.cell(len(line_number) * 1.5, 4, line_number)
                    self.pdf.cell(0, 4, clean_line, ln=True)
                else:
                    # Linea lunga - dividi in più righe
                    line_number = f'{i:4d}|'
                    indent_spaces = " " * len(line_number)
                    
                    # Prima parte
                    self.pdf.set_font('Courier', '', 8)
                    self.pdf.cell(len(line_number) * 1.5, 4, line_number)
                    self.pdf.cell(0, 4, clean_line[:MAX_LINE_WIDTH], ln=True)
                    
                    # Parti successive
                    remaining_text = clean_line[MAX_LINE_WIDTH:]
                    while remaining_text:
                        segment_width = MAX_LINE_WIDTH - len(line_number) + 3
                        if len(remaining_text) > segment_width:
                            segment = remaining_text[:segment_width]
                            remaining_text = remaining_text[segment_width:]
                        else:
                            segment = remaining_text
                            remaining_text = ""
                        
                        self.pdf.set_font('Courier', '', 8)
                        self.pdf.cell(len(line_number) * 1.5, 4, indent_spaces)
                        self.pdf.cell(0, 4, segment, ln=True)
            
            self.pdf.ln(5)
            
        except Exception as e:
            # In caso di errore, aggiungi un messaggio di errore
            self.pdf.add_page()
            self.pdf.set_font('Arial', 'B', 14)
            self.pdf.cell(0, 10, f'File: {relative_path}', ln=True)
            self.pdf.ln(5)
            self.pdf.set_font('Arial', '', 10)
            self.pdf.cell(0, 10, f'Errore nella lettura del file: {str(e)}', ln=True)
    
    def _read_file_content(self, file_path):
        """Legge il contenuto del file provando diverse codifiche"""
        for encoding in SUPPORTED_ENCODINGS:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    return file.read()
            except (UnicodeDecodeError, Exception):
                continue
        
        # Se nessuna codifica funziona, restituisci messaggio di errore
        return f'Impossibile leggere il file {file_path} - formato binario o codifica sconosciuta'
    
    def _clean_text(self, text):
        """Pulisce il testo per la compatibilità PDF"""
        try:
            text.encode('latin-1')
            return text
        except UnicodeEncodeError:
            cleaned_text = text.encode('latin-1', errors='replace').decode('latin-1')
            return cleaned_text