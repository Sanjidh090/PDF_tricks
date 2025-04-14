import pdfplumber

with pdfplumber.open("file.pdf") as pdf, open("output.txt", "w", encoding="utf-8") as f:
    
    for page in pdf.pages:
        t = page.extract_text()
        if t:
            f.write(t + '\n')
