from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import inch

# Function to create a 100-page PDF with a decorated first page
def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Draw a decorative border around the first page
    c.setStrokeColor(colors.black)
    c.setLineWidth(4)
    c.rect(20, 20, width - 40, height - 40)

    # Draw a decorative pattern (simple diagonal lines here)
    c.setStrokeColor(colors.red)
    c.setLineWidth(1)
    for i in range(0, int(width), 50):
        c.line(i, 0, i + 50, height)

    # Adding a custom title with a large font size
    c.setFont("Helvetica-Bold", 36)
    c.drawString(100, height - 100, "Decorated First Page")

    # Adding a custom subtitle with a different font style
    c.setFont("Helvetica-Oblique", 20)
    c.drawString(100, height - 150, "Welcome to a beautiful PDF")

    # Add some text in different locations
    c.setFont("Times-Roman", 12)
    c.drawString(100, height - 200, "This is the first page with decorative elements.")
    c.drawString(100, height - 220, "You can add borders, images, custom fonts, and more!")

    # Adding an image (Optional, make sure to replace 'image.jpg' with a valid image file path)
    # c.drawImage("image.jpg", 100, height - 300, width=150, height=150)

    # Add a decorative circle or other shapes
    c.setFillColor(colors.blue)
    c.circle(400, height - 400, 50, fill=1)

    # Add some text in a paragraph style (using Paragraph from Platypus)
    styles = getSampleStyleSheet()
    style = ParagraphStyle(name='Normal', fontSize=14, textColor=colors.darkblue)
    paragraph = Paragraph("This is a more advanced example of a decorated first page.", style)
    paragraph.wrapOn(c, width - 40, height - 240)
    paragraph.drawOn(c, 100, height - 270)

    # Create the first page and then add 99 empty pages
    c.showPage()  # This saves the first page
    for _ in range(99):
        c.showPage()  # Creates an empty page

    # Save the PDF
    c.save()

# Call the function to create the decorated PDF
create_pdf("decorated_example.pdf")
