#!/usr/bin/env python3
#!/usr/bin/env python3
import argparse
from docx import Document
from datetime import datetime
import sys


def find_or_create_section(document, section_title):
    """
    Find the paragraph object for a section title or create a new section if not found.
    """
    for paragraph in document.paragraphs:
        if paragraph.text == section_title and paragraph.style == document.styles['Heading 1']:
            return paragraph
    # If section not found, add it at the end of the document
    return document.add_heading(section_title, level=1)


def append_to_section(doc_path, section_title, content):
    try:
        doc = Document(doc_path)
    except Exception:
        doc = Document()
        doc.add_heading(f"Penetration Testing {datetime.now().strftime('%Y-%m-%d')}", 0)

    section_paragraph = find_or_create_section(doc, section_title)

    # Insert the content after the section title
    doc.add_paragraph(content)
    doc.save(doc_path)


def main():
    parser = argparse.ArgumentParser(description="Generate a report from findings")
    parser.add_argument("-o", "--output", help="Output document name (default: pentest-<current date>.docx)")
    parser.add_argument("-s", "--section", default="Untitled", help="Section name under which to append findings (default: Untitled)")
    args = parser.parse_args()

    output_file = args.output if args.output else f"pentest-{datetime.now().strftime('%Y-%m-%d')}.docx"

    if not sys.stdin.isatty():
        # Handling piped input
        for line in sys.stdin:
            finding = line.strip()
            if finding:
                append_to_section(output_file, args.section, finding)
                print(f"Appended finding to section '{args.section}' in {output_file}", file=sys.stderr)
    else:
        # Handling direct input
        print("Enter your finding (Ctrl+D to finish):", file=sys.stderr)
        while True:
            try:
                line = input()
                finding = line.strip()
                if finding:
                    append_to_section(output_file, args.section, finding)
                    print(f"Appended finding to section '{args.section}' in {output_file}", file=sys.stderr)
            except EOFError:
                break


if __name__ == "__main__":
    main()
