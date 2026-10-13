import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import fitz
except ImportError:
    install('PyMuPDF')
    import fitz

def extract_text(pdf_path, txt_path):
    try:
        doc = fitz.open(pdf_path)
        with open(txt_path, 'w', encoding='utf-8') as f:
            for page in doc:
                f.write(page.get_text())
        print(f"Extracted {pdf_path}")
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")

extract_text('liquidacion_visa_    1908_2026-04.pdf', 'visa_text.txt')
extract_text('liquidacion_mastercard_    3760_2026-04.pdf', 'master_text.txt')
