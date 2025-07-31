# LlamaParse Document Converter

This script converts documents from `input/reference_documents/original` to markdown format using the [LlamaParse API](https://github.com/run-llama/llama_parse) and saves them in `input/reference_documents/plain_text`.

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get LlamaParse API Key

1. Go to [LlamaCloud](https://cloud.llamaindex.ai/)
2. Sign up or log in
3. Get your API key

### 3. Configure Environment

Create a `.env` file in the `code/` directory:

```bash
# code/.env
LLAMAPARSE_API_KEY=your_actual_api_key_here
```

## Usage

Run the script from the project root:

```bash
# Convert only new files (skip already converted)
python code/llamaparse.py

# Force reconvert all files (including already converted ones)
python code/llamaparse.py --force

# Show help
python code/llamaparse.py --help
```

## Supported File Types

The script supports a wide range of document formats including:
- **Documents**: PDF, Word (`.docx`, `.doc`), RTF, Pages
- **Presentations**: PowerPoint (`.pptx`, `.ppt`), Keynote 
- **Spreadsheets**: Excel (`.xlsx`, `.xls`), CSV, Numbers
- **Images**: JPEG, PNG, GIF, BMP, SVG, TIFF, WebP
- **Web**: HTML, HTM
- **Text**: TXT, XML, EPUB
- **Audio**: MP3, MP4, WAV, WebM (up to 20MB)

## Premium Parsing

Files starting with "DIFFICULT" automatically use premium parsing with:
- Enhanced accuracy for complex layouts
- Better table structure preservation  
- Improved handling of charts and diagrams
- Advanced multi-column layout processing
- Superior mathematical formula extraction

## Features

- **Smart Processing**: Skips already converted files automatically
- **Force Reconversion**: Optional `--force` flag to reconvert all files
- **Premium Parsing**: Files starting with "DIFFICULT" use enhanced parsing
- **Recursive Processing**: Processes files in all subdirectories
- **Structure Preservation**: Maintains original folder structure in output
- **Error Handling**: Continues processing even if some files fail
- **Progress Logging**: Shows detailed progress and conversion results
- **Rate Limiting**: Includes delays to respect API limits
- **Async Processing**: Uses async operations for better performance

## Output

- Converted markdown files are saved in `input/reference_documents/plain_text/`
- Original folder structure is preserved
- File extensions are changed to `.md`
- Conversion summary is displayed at the end

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `.env` file exists and contains the correct API key
2. **Import Error**: Install dependencies with `pip install -r requirements.txt`
3. **File Not Found**: Ensure documents exist in `input/reference_documents/original/`
4. **Rate Limiting**: The script includes delays, but you may need to adjust for heavy usage

### Logs

The script provides detailed logging to help troubleshoot issues:
- Info level: Shows progress and successful conversions
- Warning level: Shows failed conversions with reasons
- Error level: Shows critical errors

## Example Output

```
2024-01-01 10:00:00 - INFO - Input directory: /path/to/input/reference_documents/original
2024-01-01 10:00:00 - INFO - Output directory: /path/to/input/reference_documents/plain_text
2024-01-01 10:00:00 - INFO - API key loaded successfully
2024-01-01 10:00:00 - INFO - LlamaParse initialized
2024-01-01 10:00:00 - INFO - Premium LlamaParse parser initialized
2024-01-01 10:00:00 - INFO - Found 5 files to process
2024-01-01 10:00:01 - INFO - Skipped (already converted): document1.pdf -> document1.md
2024-01-01 10:00:01 - INFO - Processing (premium): DIFFICULT_financial_report.pdf
2024-01-01 10:00:15 - INFO - Converted (premium): DIFFICULT_financial_report.pdf -> DIFFICULT_financial_report.md
2024-01-01 10:00:16 - INFO - Processing (standard): document3.docx
2024-01-01 10:00:20 - INFO - Converted (standard): document3.docx -> document3.md
...
2024-01-01 10:01:00 - INFO - Conversion Summary:
2024-01-01 10:01:00 - INFO - Newly converted: 3
2024-01-01 10:01:00 - INFO - Skipped (already converted): 1
2024-01-01 10:01:00 - INFO - Failed: 1
2024-01-01 10:01:00 - INFO - Premium parsing used: 1
2024-01-01 10:01:00 - INFO - Total files processed: 5

2024-01-01 10:01:00 - INFO - Files processed with premium parsing:
2024-01-01 10:01:00 - INFO -   DIFFICULT_financial_report.pdf
``` 