import os
import pytest
from main_classes.pdf_parser import PDFParser
non_existent_pdf_path = os.path.join(os.path.dirname(__file__), "non_existent.pdf")

def test_parser_invalid_path():
    with pytest.raises(FileNotFoundError):
        PDFParser.parse(non_existent_pdf_path)