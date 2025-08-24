#!/usr/bin/env python3
"""
Professional Makeup Price Chart Generator
Creates a modern, eye-catching PDF for Makeovers_by_Khushinigam
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

class MakeupPriceChartGenerator:
    def __init__(self):
        self.filename = "Makeovers_by_Khushinigam_Price_Chart.pdf"
        self.business_name = "Makeovers by Khushinigam"
        self.tagline = "Professional Makeup Services"
        
        # Modern color scheme - trending 2024 colors
        self.primary_color = colors.Color(0.7, 0.4, 0.7)  # Soft purple
        self.secondary_color = colors.Color(0.9, 0.7, 0.8)  # Light pink
        self.accent_color = colors.Color(0.2, 0.2, 0.3)  # Dark charcoal
        self.gold_color = colors.Color(0.8, 0.7, 0.3)  # Gold accent
        self.background_color = colors.Color(0.98, 0.96, 0.98)  # Very light pink
        
        # Makeup services and prices
        self.services = [
            ("Regular", "₹1,500"),
            ("HD", "₹2,000"),
            ("Signature", "₹4,000"),
            ("Signature (International)", "₹5,000")
        ]

    def create_pdf(self):
        # Create the PDF document
        doc = SimpleDocTemplate(
            self.filename,
            pagesize=A4,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch
        )
        
        # Build the story (content)
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=28,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=self.primary_color,
            fontName='Helvetica-Bold'
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=self.accent_color,
            fontName='Helvetica-Oblique'
        )
        
        section_title_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading2'],
            fontSize=20,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=self.accent_color,
            fontName='Helvetica-Bold'
        )
        
        # Header section
        story.append(Spacer(1, 0.5*inch))
        
        # Business name
        title = Paragraph(self.business_name, title_style)
        story.append(title)
        
        # Tagline
        subtitle = Paragraph(self.tagline, subtitle_style)
        story.append(subtitle)
        
        # Decorative line
        story.append(Spacer(1, 20))
        
        # Section title
        section_title = Paragraph("Party Makeup Price List", section_title_style)
        story.append(section_title)
        
        story.append(Spacer(1, 30))
        
        # Create the price table
        table_data = [
            ["Service Type", "Price"],
        ]
        
        # Add services to table
        for service, price in self.services:
            table_data.append([service, price])
        
        # Create table
        table = Table(table_data, colWidths=[3*inch, 1.5*inch])
        
        # Style the table
        table.setStyle(TableStyle([
            # Header row
            ('BACKGROUND', (0, 0), (-1, 0), self.primary_color),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            
            # Data rows
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 1), (-1, -1), self.accent_color),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            
            # Alternating row colors
            ('BACKGROUND', (0, 2), (-1, 2), self.secondary_color),
            ('BACKGROUND', (0, 4), (-1, 4), self.secondary_color),
            
            # Grid and borders
            ('GRID', (0, 0), (-1, -1), 1, self.primary_color),
            ('LINEBELOW', (0, 0), (-1, 0), 2, self.accent_color),
            
            # Padding
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ]))
        
        story.append(table)
        story.append(Spacer(1, 40))
        
        # Additional information
        info_style = ParagraphStyle(
            'Info',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_CENTER,
            textColor=self.accent_color,
            fontName='Helvetica-Oblique'
        )
        
        info_text = [
            "• All prices are inclusive of makeup application and basic styling",
            "• HD makeup includes high-definition products for photography",
            "• Signature services include premium products and extended styling",
            "• International Signature includes luxury imported cosmetics",
            "• Additional charges may apply for travel beyond city limits"
        ]
        
        for text in info_text:
            story.append(Paragraph(text, info_style))
            story.append(Spacer(1, 8))
        
        story.append(Spacer(1, 30))
        
        # Contact section
        contact_style = ParagraphStyle(
            'Contact',
            parent=styles['Normal'],
            fontSize=12,
            alignment=TA_CENTER,
            textColor=self.primary_color,
            fontName='Helvetica-Bold'
        )
        
        contact = Paragraph("For bookings and inquiries, contact Makeovers by Khushinigam", contact_style)
        story.append(contact)
        
        # Footer
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=8,
            alignment=TA_CENTER,
            textColor=self.accent_color,
            fontName='Helvetica'
        )
        
        story.append(Spacer(1, 20))
        footer = Paragraph("Professional Makeup Services • Creating Beautiful Transformations", footer_style)
        story.append(footer)
        
        # Build PDF
        doc.build(story)
        print(f"✨ Successfully created {self.filename}")
        return self.filename

def main():
    generator = MakeupPriceChartGenerator()
    pdf_file = generator.create_pdf()
    
    # Check if file was created successfully
    if os.path.exists(pdf_file):
        file_size = os.path.getsize(pdf_file)
        print(f"📄 PDF created: {pdf_file}")
        print(f"📊 File size: {file_size} bytes")
        print(f"🎨 Features: Modern design with trending colors and professional layout")
    else:
        print("❌ Error: PDF file was not created")

if __name__ == "__main__":
    main()