from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class PDFGenerator:
    def __init__(self, logger):
        self.logger = logger

    def generate_pdf(self, pod_data, output_path):
        """Generate a PDF file from the Proof of Delivery data."""
        try:
            doc = SimpleDocTemplate(output_path, pagesize=letter)
            story = []
            styles = getSampleStyleSheet()

            # Add title
            story.append(Paragraph("Proof of Delivery", styles['Title']))
            story.append(Spacer(1, 12))

            # Add tracking number
            story.append(Paragraph(f"Tracking Number: {pod_data['trackingNumber']}", styles['Heading2']))
            story.append(Spacer(1, 12))

            # Add shipment information
            story.append(Paragraph("Shipment Information:", styles['Heading3']))
            story.append(Paragraph(f"Status: {pod_data['packageStatus']}", styles['Normal']))
            story.append(Paragraph(f"Service: {pod_data['service']}", styles['Normal']))
            story.append(Paragraph(f"Weight: {pod_data['weight']} {pod_data['weightUnit']}", styles['Normal']))
            story.append(Spacer(1, 12))

            # Add delivery information
            story.append(Paragraph("Delivery Information:", styles['Heading3']))
            story.append(Paragraph(f"Delivered On: {pod_data['deliveredOn']}", styles['Normal']))
            story.append(Paragraph(f"Signed By: {pod_data['signedBy']}", styles['Normal']))
            story.append(Spacer(1, 12))

            # Build the PDF
            doc.build(story)
            self.logger.info(f"Successfully generated PDF at {output_path}")
        except Exception as e:
            self.logger.error(f"Failed to generate PDF: {str(e)}")
            raise
