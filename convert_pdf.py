#!/usr/bin/env python3
"""
Convert PDF pages to images for seamless website display
Also generates the HTML file with all pages
"""

import fitz  # PyMuPDF
import os
from pathlib import Path

def convert_pdf_to_images(pdf_path, output_dir="pages", dpi=150):
    """
    Convert PDF pages to high-quality images and generate HTML
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the images
        dpi: Resolution for the images (higher = better quality but larger files)
    """
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Open PDF
    pdf_document = fitz.open(pdf_path)
    total_pages = len(pdf_document)
    
    print(f"📄 Converting {total_pages} pages from {pdf_path}...")
    
    page_paths = []
    
    # Convert each page to image
    for page_num in range(total_pages):
        page = pdf_document[page_num]
        
        # Render page to image (pixmap)
        # Scale factor: dpi/72 (default PDF resolution is 72 DPI)
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        # Save as PNG
        page_filename = f"page_{page_num + 1:03d}.png"
        output_path = os.path.join(output_dir, page_filename)
        pix.save(output_path)
        page_paths.append(f"{output_dir}/{page_filename}")
        
        print(f"  ✓ Page {page_num + 1}/{total_pages} saved as {output_path}")
    
    pdf_document.close()
    print(f"\n✅ Conversion complete! {total_pages} pages saved to '{output_dir}/'")
    
    # Generate HTML
    generate_html(page_paths)
    
    return total_pages

def generate_html(page_paths):
    """Generate HTML file with all PDF pages as images"""
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brews, Bakes & Brushes</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html, body {
            width: 100%;
            overflow-x: hidden;
            overflow-y: auto;
            background: transparent;
        }

        body {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .page {
            width: 100%;
            max-width: 100vw;
            display: block;
            margin: 0;
            padding: 0;
        }

        .page img {
            width: 100%;
            height: auto;
            display: block;
            margin: 0;
            padding: 0;
            max-width: 100%;
        }
    </style>
</head>
<body>
'''
    
    # Add each page as an image
    for i, page_path in enumerate(page_paths, 1):
        html_content += f'''    <div class="page">
        <img src="{page_path}" alt="Page {i}" loading="lazy">
    </div>
'''
    
    html_content += '''</body>
</html>'''
    
    # Write HTML file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ HTML file generated: index.html")

if __name__ == "__main__":
    pdf_file = "Brews, Bakes & Brushes (1).pdf"
    
    if not os.path.exists(pdf_file):
        print(f"❌ Error: PDF file '{pdf_file}' not found!")
        exit(1)
    
    convert_pdf_to_images(pdf_file)