from PyPDF2 import PdfMerger

def merge_pdfs(pdf1_path, pdf2_path, output_pdf_path):
    merger = PdfMerger()
    
    # Append both PDFs to the merger
    merger.append(pdf1_path)
    merger.append(pdf2_path)
    
    # Write the merged PDF to the output file
    with open(output_pdf_path, 'wb') as output_pdf:
        merger.write(output_pdf)
    
    # Close the merger
    merger.close()

# Example usage: provide paths to the two PDF files
merge_pdfs(r"C:\Users\sanji\Downloads\pdfsplit_project\economics.pdf",r"C:\Users\sanji\Downloads\pdfsplit_project\HUM qs 1.2.pdf",r"c:\Users\sanji\Downloads\pdfsplit_project\Hum-1-2-2021.pdf")
## Ctrl+ Shift + C for copying path of a file
