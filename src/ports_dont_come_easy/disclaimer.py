#!/home/kirilla/ws/python/venv/bin/python3
#!/usr/bin/env python3
import argparse
from docx import Document
from datetime import datetime
import sys


def add_disclaimer_section(doc_path, disclaimer_text):
    """Add a disclaimer section to the document."""
    try:
        doc = Document(doc_path)
    except FileNotFoundError:
        doc = Document()
        doc.add_heading('Disclaimer', level=1)
    else:
        doc.add_page_break()  # Add a page break before the disclaimer for readability
        doc.add_heading('Disclaimer', level=1)

    doc.add_paragraph(disclaimer_text)
    doc.save(doc_path)


def main():
    parser = argparse.ArgumentParser(description="Add a disclaimer section to the pentest report")
    parser.add_argument("-o", "--output", help="Output document name (default: pentest-<current date>.docx)", default=f"pentest-{datetime.now().strftime('%Y-%m-%d')}.docx")
    args = parser.parse_args()

    # Disclaimer text (customize as needed)
    disclaimer_text = "The findings in this report are for authorized use only. The methodologies used are intended for educational purposes and should not be used maliciously."

    add_disclaimer_section(args.output, disclaimer_text)
    print(f"Disclaimer section added to '{args.output}'.", file=sys.stderr)


if __name__ == "__main__":
    main()
