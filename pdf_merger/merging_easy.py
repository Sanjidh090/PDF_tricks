from pypdf import PdfWriter

pdfs = ['IEM CPM & PERT class note.pdf', 'IEM CPM & PERT Extra Note.pdf', 'IEM MRP Class note.pdf', 'IEM MRP Extra Note.pdf','IEM Scheduling Class Note.pdf','IEM sequencing Extra Note.pdf','IEM Facilty Location class note.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("iem_merged.pdf")
merger.close()