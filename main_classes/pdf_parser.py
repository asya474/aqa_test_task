import os
import pdfplumber
from typing import Dict


class PDFParser:
    @staticmethod
    def parse(pdf_path: str) -> Dict[str, str]:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        result = {}
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        for line in text.split('\n'):
                            if ':' in line:
                                key_part, *value_part = line.split(':', 1)
                                key = key_part.strip()
                                value = value_part[0].strip() if value_part else ''
                                if key in result:
                                    result[key] += f", {value}"
                                else:
                                    result[key] = value
        except Exception as e:
            raise ValueError(f"PDF parsing failed: {str(e)}")
        return result