#!/home/kirilla/ws/python/venv/bin/python3
#!/usr/bin/env python3
import argparse
from docx import Document
from datetime import datetime
import sys
import os


def update_document_title(doc, title_text):
    """Update the document title if it exists, or add a new title."""
    title_updated = False
    for paragraph in doc.paragraphs:
        if paragraph.style.name == 'Title':
            paragraph.text = title_text
            title_updated = True
            break

    # If no title paragraph with 'Title' style was found, add a new title at the beginning of the document.
    if not title_updated:
        doc.add_paragraph(title_text, style='Title')


def add_custom_header(doc_path, client_name):
    """Add or update the document title with custom information."""
    title_text = f"Penetration Testing {datetime.now().strftime('%Y-%m-%d')} - Client: {client_name}"

    # Check if the document exists to decide on opening or creating a new one.
    if os.path.exists(doc_path):
        doc = Document(doc_path)
    else:
        doc = Document()

    update_document_title(doc, title_text)
    doc.save(doc_path)


def main():
    parser = argparse.ArgumentParser(description="Update document with custom client title")
    parser.add_argument("-o", "--output", help="Output document name (default: pentest-<current date>.docx)", default=f"pentest-{datetime.now().strftime('%Y-%m-%d')}.docx")
    parser.add_argument("client", help="Client name to include in the document title")
    args = parser.parse_args()

    add_custom_header(args.output, args.client)
    print(f"Document '{args.output}' updated with custom client title.", file=sys.stderr)


if __name__ == "__main__":
    main()
