!pip install python-docs(google koro)
from docx import Document

def remove_last_page(docx_file, output_file):
    # Load the .docx file
    doc = Document(docx_file)

    # We'll try to estimate a "page" by removing the last few paragraphs
    # A simple way could be to remove, say, the last 5 paragraphs
    paragraphs = doc.paragraphs
    num_paragraphs = len(paragraphs)

    # Remove the last "few" paragraphs (this number can be adjusted)
    num_to_remove = 5  # You can change this value based on the number of paragraphs in the last page
    for _ in range(num_to_remove):
        if paragraphs:
            # Remove the last paragraph
            p = paragraphs[-1]
            p.clear()

    # Save the modified document
    doc.save(output_file)

# Usage example
remove_last_page(r"C:\Users\sanji\Downloads\Al-Khwarizmi(1).docx",r"C:\Users\sanji\Downloads\Al-Khwarizmi(cleaned).docx")
