#!/usr/bin/env python3
"""
Makeup Price Chart Generator
Creates a beautiful, trendy PDF price chart for makeup services
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def create_makeup_price_chart():
    """Create a trendy makeup price chart PDF"""
    
    # Create the PDF document
    filename = "Makeovers_by_Khushinigam.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    
    # Define custom styles
    styles = getSampleStyleSheet()
    
    # Custom title style with gradient effect simulation
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=colors.HexColor('#FF6B9D'),  # Trendy pink
        alignment=TA_CENTER,
        spaceAfter=30,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=16,
        textColor=colors.HexColor('#8A2BE2'),  # Trendy purple
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica'
    )
    
    # Service name style
    service_style = ParagraphStyle(
        'ServiceStyle',
        parent=styles['Normal'],
        fontSize=18,
        textColor=colors.HexColor('#2C3E50'),  # Dark blue-gray
        alignment=TA_LEFT,
        fontName='Helvetica-Bold',
        spaceAfter=5
    )
    
    # Price style
    price_style = ParagraphStyle(
        'PriceStyle',
        parent=styles['Normal'],
        fontSize=20,
        textColor=colors.HexColor('#E74C3C'),  # Trendy red
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Build the story
    story = []
    
    # Add title with emoji
    title = Paragraph("💄 Makeovers by Khushinigam 💄", title_style)
    story.append(title)
    
    # Add subtitle
    subtitle = Paragraph("Professional Makeup Services & Pricing", subtitle_style)
    story.append(subtitle)
    
    # Add decorative line
    story.append(Spacer(1, 20))
    
    # Create the pricing table
    data = [
        ['Service Type', 'Price (₹)'],
        ['Regular Makeup', '₹1,500'],
        ['HD Makeup', '₹2,000'],
        ['Signature Makeup', '₹4,000'],
        ['Signature (International)', '₹5,000']
    ]
    
    # Create table with custom styling
    table = Table(data, colWidths=[4*inch, 2*inch])
    
    # Define table style with trendy colors
    table_style = TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B9D')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 16),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        
        # Service rows styling
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F8F9FA')),
        ('BACKGROUND', (1, 1), (1, -1), colors.HexColor('#FFF5F5')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2C3E50')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 14),
        ('ALIGN', (0, 1), (0, -1), 'LEFT'),
        ('ALIGN', (1, 1), (1, -1), 'CENTER'),
        ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
        
        # Borders
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E9ECEF')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8F9FA')]),
        
        # Padding
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ('RIGHTPADDING', (0, 0), (-1, -1), 15),
    ])
    
    table.setStyle(table_style)
    story.append(table)
    
    # Add spacing
    story.append(Spacer(1, 30))
    
    # Add additional information
    info_style = ParagraphStyle(
        'InfoStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#6C757D'),
        alignment=TA_CENTER,
        fontName='Helvetica',
        spaceAfter=10
    )
    
    info1 = Paragraph("✨ Professional makeup artists with years of experience", info_style)
    info2 = Paragraph("🎨 High-quality products and latest techniques", info_style)
    info3 = Paragraph("📱 Book your appointment today!", info_style)
    
    story.append(info1)
    story.append(info2)
    story.append(info3)
    
    # Add contact information
    story.append(Spacer(1, 20))
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#8A2BE2'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=5
    )
    
    contact = Paragraph("📞 Contact: +91-XXXXXXXXXX | 📧 Email: info@khushinigam.com", contact_style)
    story.append(contact)
    
    # Build the PDF
    doc.build(story)
    
    print(f"✅ PDF created successfully: {filename}")
    return filename

if __name__ == "__main__":
    try:
        filename = create_makeup_price_chart()
        print(f"🎉 Your makeup price chart '{filename}' is ready!")
        print("📁 Check your current directory for the PDF file.")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")