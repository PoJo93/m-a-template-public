# Input Directory

This directory contains the source materials for generating Company Information Memorandums (CIM).

## Structure

### reference_documents/
Place your company documents here for analysis:

#### original/
- Upload original documents (PDFs, DOCX, etc.)
- These will be processed by `code/llamaparse.py`

#### plain_text/
- Converted documents will appear here after processing
- Used as input for CIM generation

#### past_cim_examples/
- Reference examples of high-quality CIMs
- Used as style templates

### projektkommentare.md
- Project-specific comments and notes
- Team briefings and requirements

## Usage

1. Upload company documents to `reference_documents/original/`
2. Run `python code/llamaparse.py` to convert documents
3. Add any project notes to `projektkommentare.md`
4. Proceed with CIM generation

## Security Note

All files in this directory contain proprietary information and are excluded from version control. 