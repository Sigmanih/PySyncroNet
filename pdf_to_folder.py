#File: pdf_to_folder.py
import re
import os
import PyPDF2
from pathlib import Path
import datetime

class UniversalPDFToProject:
    def __init__(self):
        self.files_data = {}
        self.metadata = {}
        
    def extract_pdf_content(self, pdf_path):
        """Estrae il contenuto dal PDF con gestione errori migliorata"""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                full_text = ""
                
                for page_num, page in enumerate(pdf_reader.pages):
                    page_text = page.extract_text()
                    full_text += page_text + "\n"
                
                return full_text
        except Exception as e:
            print(f"❌ Errore nell'estrazione del PDF: {e}")
            return None

    def parse_files_from_pdf(self, pdf_text):
        """Analizza il PDF e estrae i file PRESERVANDO GLI SPAZI"""
        lines = pdf_text.split('\n')
        current_file = None
        current_content = []
        reading_file_content = False
        
        for line in lines:
            # PRESERVA la linea originale - NO strip()
            raw_line = line
            
            # Cerca l'inizio di un nuovo file
            if raw_line.strip().startswith('File:'):
                # Salva il file precedente se esiste
                if current_file and current_content:
                    full_content = '\n'.join(current_content)
                    if full_content.strip():
                        self.files_data[current_file] = full_content
                
                # Inizia un nuovo file
                file_path = raw_line.strip()[5:].strip()
                current_file = file_path
                current_content = []
                reading_file_content = True
                continue
            
            # Se stiamo leggendo il contenuto di un file
            if reading_file_content and current_file:
                # Controlla se è la fine della sezione file
                stripped_check = raw_line.strip()
                if (stripped_check.startswith('DOCUMENTAZIONE') or 
                    stripped_check.startswith('Cartelle') or 
                    stripped_check.startswith('File') or 
                    stripped_check.startswith('Estensioni') or
                    stripped_check.startswith('Progetto:') or 
                    stripped_check.startswith('Cartella:')):
                    reading_file_content = False
                    continue
                
                # Gestisce le linee numerate PRESERVANDO GLI SPAZI
                line_match = re.match(r'^\s*(\d+)\s*\|\s*(.*)$', raw_line)
                if line_match:
                    # PRENDI IL CONTENUTO ESATTAMENTE COME È, CON GLI SPAZI
                    content_part = line_match.group(2)
                    current_content.append(content_part)
        
        # Salva l'ultimo file
        if current_file and current_content:
            full_content = '\n'.join(current_content)
            if full_content.strip():
                self.files_data[current_file] = full_content
        
        return self.files_data

    def reconstruct_indentation(self, content):
        """Ricostruisce l'indentazione basata sul conteggio ESATTO degli spazi"""
        if not content:
            return content
        
        lines = content.split('\n')
        reconstructed_lines = []
        
        for line in lines:
            if not line.strip():  # Linea vuota
                reconstructed_lines.append('')
                continue
            
            # Conta ESATTAMENTE gli spazi all'inizio della linea
            space_count = 0
            for char in line:
                if char == ' ':
                    space_count += 1
                else:
                    break
            
            # Calcola i livelli di indentazione (4 spazi = 1 livello)
            # Arrotonda per eccesso per gestire spazi residui
            indent_level = (space_count + 3) // 4
            
            # Ricostruisce con 4 spazi per livello
            reconstructed_line = ('    ' * indent_level) + line.lstrip()
            reconstructed_lines.append(reconstructed_line)
        
        return '\n'.join(reconstructed_lines)

    def clean_file_content(self, content, file_extension):
        """Pulisce il contenuto preservando e ricostruendo l'indentazione"""
        if not content:
            return content
        
        # Rimuove i tag [troncato] se presenti
        content = content.replace('... [troncato]', '')
        
        # PER TUTTI I FILE: ricostruisci l'indentazione dagli spazi
        content = self.reconstruct_indentation(content)
        
        return content

    def get_file_extension(self, file_path):
        """Restituisce l'estensione del file"""
        path = Path(file_path)
        return path.suffix.lower()

    def recreate_project_structure(self, pdf_path, output_folder):
        """Ricrea l'intera struttura del progetto dal PDF"""
        print(f"📖 Leggendo il PDF: {pdf_path}")
        pdf_text = self.extract_pdf_content(pdf_path)
        
        if not pdf_text:
            print("❌ Impossibile leggere il PDF")
            return False
        
        print("🔍 Analizzando il contenuto del PDF...")
        files_data = self.parse_files_from_pdf(pdf_text)
        
        if not files_data:
            print("❌ Nessun file trovato nel PDF")
            return False
        
        print(f"📁 Trovati {len(files_data)} file nel PDF")
        
        output_path = Path(output_folder)
        output_path.mkdir(parents=True, exist_ok=True)
        
        files_created = 0
        errors = []
        
        for file_path, raw_content in files_data.items():
            try:
                full_path = output_path / file_path
                
                # Crea le directory necessarie
                full_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Ottieni l'estensione del file
                file_extension = self.get_file_extension(file_path)
                
                # Pulisci il contenuto preservando l'indentazione
                cleaned_content = self.clean_file_content(raw_content, file_extension)
                
                # Scrivi il file
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                files_created += 1
                print(f"✅ Creato: {file_path}")
                
            except Exception as e:
                error_msg = f"❌ Errore con {file_path}: {str(e)}"
                errors.append(error_msg)
                print(error_msg)
        
        # Scrivi un report di ricostruzione
        self.write_reconstruction_report(output_path, files_created, errors, files_data)
        
        print(f"\n🎉 Ricostruzione completata!")
        print(f"📊 File creati: {files_created}")
        print(f"❌ Errori: {len(errors)}")
        print(f"📂 Output: {output_path.absolute()}")
        
        if errors:
            print("\nErrori riscontrati:")
            for error in errors:
                print(f"  - {error}")
        
        return True

    def write_reconstruction_report(self, output_path, files_created, errors, files_data):
        """Scrive un report dettagliato della ricostruzione"""
        report_content = f"""RICOSTRUZIONE PROGETTO DA PDF
===============================

Data ricostruzione: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
File creati con successo: {files_created}
Errori riscontrati: {len(errors)}

DETTAGLIO FILE RICOSTRUITI:
---------------------------
"""

        for file_path in sorted(files_data.keys()):
            file_extension = self.get_file_extension(file_path)
            content_length = len(files_data[file_path])
            report_content += f"- {file_path} ({file_extension}, {content_length} caratteri)\n"

        if errors:
            report_content += f"\nERRORI RISCONTRATI:\n-------------------\n"
            for error in errors:
                report_content += f"- {error}\n"

        report_content += f"""
STATISTICHE:
-----------
File totali nel PDF: {len(files_data)}
File creati: {files_created}
Success rate: {(files_created/len(files_data))*100:.1f}%

ESTENSIONI FILE RICOSTRUITE:
---------------------------
"""

        # Calcola statistiche per estensione
        extensions = {}
        for file_path in files_data.keys():
            ext = self.get_file_extension(file_path)
            extensions[ext] = extensions.get(ext, 0) + 1

        for ext, count in sorted(extensions.items()):
            report_content += f"- {ext or 'Nessuna'}: {count} file\n"

        with open(output_path / "RICOSTRUZIONE_REPORT.txt", 'w', encoding='utf-8') as f:
            f.write(report_content)

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Ricrea un intero progetto da PDF - Supporta qualsiasi tipo di file di testo/codice'
    )
    parser.add_argument('pdf_path', help='Percorso del PDF sorgente')
    parser.add_argument('output_folder', help='Cartella di destinazione per il progetto ricostruito')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf_path):
        print(f"❌ Errore: Il file PDF '{args.pdf_path}' non esiste.")
        return
    
    print("🛠️  Ricostruzione progetto da PDF")
    print("=" * 50)
    
    recreator = UniversalPDFToProject()
    success = recreator.recreate_project_structure(args.pdf_path, args.output_folder)
    
    if success:
        print("\n✅ Ricostruzione completata con successo!")
        print(f"📁 Il progetto è stato ricreato in: {args.output_folder}")
    else:
        print("\n❌ Ricostruzione fallita!")

if __name__ == "__main__":
    # Esempio di utilizzo diretto
    if len(os.sys.argv) == 1:
        print("🛠️  Ricostruzione progetto da PDF")
        print("=" * 40)
        
        pdf_file = input("Inserisci il percorso del PDF: ").strip()
        output_dir = input("Inserisci la cartella di output: ").strip()
        
        if pdf_file and output_dir:
            if os.path.exists(pdf_file):
                recreator = UniversalPDFToProject()
                recreator.recreate_project_structure(pdf_file, output_dir)
            else:
                print("❌ Il file PDF specificato non esiste.")
        else:
            print("❌ Devi specificare entrambi i percorsi.")
    else:
        main()