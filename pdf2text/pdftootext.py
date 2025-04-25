from docx import Document
from pathlib import Path

# Load the extracted text content from the PDF
pdf_text_path = "/mnt/data/law pdf.pdf"
docx_output_path = "/mnt/data/Law_Equity_Bangladesh.docx"

# Create a new Word document
doc = Document()
doc.add_heading("Law and Equity in Bangladesh", level=1)

# Read the content of the PDF as plain text (from the previous extraction)
with open(pdf_text_path, 'rb') as f:
    import fitz  # PyMuPDF
    doc_pdf = fitz.open(stream=f.read(), filetype="pdf")
    for page in doc_pdf:
        doc.add_paragraph(page.get_text())

# Save the document
doc.save(docx_output_path)

