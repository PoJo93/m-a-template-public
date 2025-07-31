#!/usr/bin/env python3
"""
LlamaParse Document Converter

This script converts documents from input/reference_documents/original 
to markdown format and saves them in input/reference_documents/plain_text

Features:
- Skips already converted files (unless --force flag is used)
- Premium parsing for files starting with "DIFFICULT"
- Maintains original directory structure
- Supports a wide range of document formats

Requirements:
- pip install llama-parse python-dotenv
- API key in code/.env as LLAMAPARSE_API_KEY

Usage:
- python code/llamaparse.py           # Convert only new files
- python code/llamaparse.py --force   # Force reconvert all files
"""

import os
import asyncio
import nest_asyncio
import argparse
from pathlib import Path
from typing import List, Tuple
import logging
from dotenv import load_dotenv

# Import LlamaParse
try:
    from llama_parse import LlamaParse
except ImportError:
    print("Error: llama-parse not installed. Please run: pip install llama-parse")
    exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Apply nest_asyncio for Jupyter/async compatibility
nest_asyncio.apply()

class DocumentConverter:
    """Handles conversion of documents using LlamaParse API"""
    
    def __init__(self, force_reconvert=False):
        self.force_reconvert = force_reconvert
        self.setup_directories()
        self.load_api_key()
        self.setup_parser()
        
    def setup_directories(self):
        """Set up input and output directory paths"""
        # Get the project root (parent of code directory)
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        
        self.input_dir = project_root / "input" / "reference_documents" / "original"
        self.output_dir = project_root / "input" / "reference_documents" / "plain_text"
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Input directory: {self.input_dir}")
        logger.info(f"Output directory: {self.output_dir}")
        
    def load_api_key(self):
        """Load API key from .env file"""
        # Load .env file from code directory
        env_path = Path(__file__).parent / ".env"
        
        if not env_path.exists():
            raise FileNotFoundError(
                f"Environment file not found at {env_path}. "
                "Please create code/.env with LLAMAPARSE_API_KEY=your_api_key"
            )
            
        load_dotenv(env_path)
        self.api_key = os.getenv("LLAMAPARSE_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "LLAMAPARSE_API_KEY not found in .env file. "
                "Please add LLAMAPARSE_API_KEY=your_api_key to code/.env"
            )
            
        logger.info("API key loaded successfully")
        
    def setup_parser(self):
        """Initialize LlamaParse with configuration"""
        self.parser = LlamaParse(
            api_key=self.api_key,
            result_type="markdown",
            verbose=True,
        )
        logger.info("LlamaParse initialized")
        
    def get_supported_files(self) -> List[Path]:
        """Get list of supported files for parsing"""
        # Common document formats supported by LlamaParse
        supported_extensions = {
            # Base types
            '.pdf',

            # Documents and presentations
            '.abw', '.cgm', '.cwk', '.doc', '.docx', '.docm', '.dot', '.dotm', '.hwp',
            '.key', '.lwp', '.mw', '.mcw', '.pages', '.pbd', '.ppt', '.pptm', '.pptx',
            '.pot', '.potm', '.potx', '.rtf', '.sda', '.sdd', '.sdp', '.sdw', '.sgl',
            '.sti', '.sxi', '.sxw', '.stw', '.sxg', '.txt', '.uof', '.uop', '.uot',
            '.vor', '.wpd', '.wps', '.xml', '.zabw', '.epub',

            # Images
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff', '.webp',
            '.web', '.htm', '.html',

            # Spreadsheets
            '.xlsx', '.xls', '.xlsm', '.xlsb', '.xlw', '.csv', '.dif', '.sylk', '.slk',
            '.prn', '.numbers', '.et', '.ods', '.fods', '.uos1', '.uos2', '.dbf',
            '.wk1', '.wk2', '.wk3', '.wk4', '.wks', '.123', '.wq1', '.wq2', '.wb1',
            '.wb2', '.wb3', '.qpw', '.xlr', '.eth', '.tsv',

            # Audio (limited to 20 MB)
            '.mp3', '.mp4', '.mpeg', '.mpga', '.m4a', '.wav', '.webm'
        }
        
        files = []
        for file_path in self.input_dir.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
                # Skip hidden files and system files
                if not file_path.name.startswith('.') and file_path.name != '.DS_Store':
                    files.append(file_path)
                    
        return files
        
    def get_output_path(self, input_file: Path) -> Path:
        """Generate output path maintaining directory structure"""
        # Get relative path from input directory
        relative_path = input_file.relative_to(self.input_dir)
        
        # Change extension to .md and create output path
        output_path = self.output_dir / relative_path.with_suffix('.md')
        
        # Create parent directories if they don't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        return output_path
        
    def is_file_already_converted(self, input_file: Path) -> bool:
        """Check if the file has already been converted to markdown"""
        if self.force_reconvert:
            return False  # Never skip if force reconvert is enabled
        output_path = self.get_output_path(input_file)
        return output_path.exists()
        
    def should_use_premium_parsing(self, input_file: Path) -> bool:
        """Check if file should use premium parsing (files starting with DIFFICULT)"""
        return input_file.name.upper().startswith('DIFFICULT')
        
    def setup_premium_parser(self):
        """Initialize LlamaParse with premium parsing configuration"""
        
        self.premium_parser = LlamaParse(
            api_key=self.api_key,
            result_type="markdown",
            verbose=True,
            premium_mode=True
        )
        logger.info("Premium LlamaParse parser initialized")
        
    def setup_parser(self):
        """Initialize LlamaParse with configuration"""
        self.parser = LlamaParse(
            api_key=self.api_key,
            result_type="markdown",
            verbose=True,
            auto_mode=True,  # Automatically choose best parsing mode for each document
        )
        logger.info("LlamaParse initialized")
        
        # Also setup premium parser for difficult files
        self.setup_premium_parser()
        
    async def convert_file(self, file_path: Path) -> Tuple[bool, str]:
        """Convert a single file to markdown"""
        try:
            # Check if file is already converted
            if self.is_file_already_converted(file_path):
                output_path = self.get_output_path(file_path)
                skip_msg = f"Skipped (already converted): {file_path} -> {output_path}"
                logger.info(skip_msg)
                return True, skip_msg
            
            # Check if this file needs premium parsing
            use_premium = self.should_use_premium_parsing(file_path)
            parser_to_use = self.premium_parser if use_premium else self.parser
            
            parsing_type = "premium" if use_premium else "auto"
            logger.info(f"Processing ({parsing_type}): {file_path}")
            
            # Parse the document
            documents = await parser_to_use.aload_data(str(file_path))
            
            if not documents:
                return False, "No content extracted"
                
            # Combine all document content (in case of multi-page documents)
            markdown_content = "\n\n".join([doc.text for doc in documents])
            
            # Get output path
            output_path = self.get_output_path(file_path)
            
            # Write markdown content
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            success_msg = f"Converted ({parsing_type}): {file_path} -> {output_path}"
            logger.info(success_msg)
            return True, str(output_path)
            
        except Exception as e:
            error_msg = f"Failed to convert {file_path}: {str(e)}"
            logger.error(error_msg)
            return False, error_msg
            
    async def convert_all_documents(self):
        """Convert all supported documents to markdown"""
        files = self.get_supported_files()
        
        if not files:
            logger.warning("No supported files found for conversion")
            return
            
        logger.info(f"Found {len(files)} files to process")
        
        # Track conversion results
        converted = 0
        skipped = 0
        failed = 0
        premium_files = 0
        results = []
        
        # Process files one by one to avoid rate limiting
        for file_path in files:
            success, result = await self.convert_file(file_path)
            results.append((file_path, success, result))
            
            if success:
                if "Skipped" in result:
                    skipped += 1
                else:
                    converted += 1
                    if self.should_use_premium_parsing(file_path):
                        premium_files += 1
            else:
                failed += 1
                
            # Add a small delay to avoid rate limiting
            await asyncio.sleep(1)
            
        # Print summary
        logger.info(f"\nConversion Summary:")
        logger.info(f"Newly converted: {converted}")
        logger.info(f"Skipped (already converted): {skipped}")
        logger.info(f"Failed: {failed}")
        logger.info(f"Premium parsing used: {premium_files}")
        logger.info(f"Total files processed: {len(files)}")
        
        # Print failed files if any
        if failed > 0:
            logger.warning("\nFailed conversions:")
            for file_path, success, result in results:
                if not success:
                    logger.warning(f"  {file_path}: {result}")
                    
        # Print premium parsing files
        if premium_files > 0:
            logger.info("\nFiles processed with premium parsing:")
            for file_path, success, result in results:
                if success and "Skipped" not in result and self.should_use_premium_parsing(file_path):
                    logger.info(f"  {file_path.name}")

async def main():
    """Main function to run the document conversion"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Convert documents to markdown using LlamaParse",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python code/llamaparse.py           # Convert only new files
  python code/llamaparse.py --force   # Force reconvert all files
        """
    )
    parser.add_argument(
        '--force', 
        action='store_true',
        help='Force reconversion of all files, even if they already exist'
    )
    
    args = parser.parse_args()
    
    try:
        converter = DocumentConverter(force_reconvert=args.force)
        
        if args.force:
            logger.info("Force reconversion enabled - all files will be reconverted")
        else:
            logger.info("Smart processing enabled - skipping already converted files")
        
        await converter.convert_all_documents()
        logger.info("Document conversion completed!")
        
    except Exception as e:
        logger.error(f"Error during conversion: {str(e)}")
        return 1
        
    return 0

if __name__ == "__main__":
    # Run the async main function
    exit_code = asyncio.run(main())
    exit(exit_code)
