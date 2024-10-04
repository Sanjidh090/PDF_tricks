from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path):
    reader = PdfReader(input_pdf_path)
    
    # Define the ranges and filenames
    split_ranges = [
        (0, 2, 'math.pdf'),           # Pages 1-2 for Math
        (2, 4, 'physics.pdf'),        # Pages 3-4 for Physics
        (4, 7, 'mechanical.pdf'),     # Pages 5-7 for Mechanical
        (7, 10, 'economics.pdf'),     # Pages 8-10 for Economics
        (10, len(reader.pages), 'eee.pdf') # The rest for EEE
    ]
    
    for start, end, output_name in split_ranges:
        writer = PdfWriter()
        
        # Add the specified range of pages
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])
        
        # Write the split part to a new PDF
        with open(output_name, 'wb') as output_pdf:
            writer.write(output_pdf)

# Example usage
split_pdf(r"C:\Users\sanji\Downloads\2k21 1-2 que.pdf")
