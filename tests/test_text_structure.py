import os
import re
from main_classes.pdf_parser import PDFParser
pdf_path = os.path.join(os.path.dirname(__file__), "test_task.pdf")

def test_text_structure(reference_data):
    test_data = PDFParser.parse(pdf_path)
    date_pattern = r'\d{2}\.\d{2}\.\d{4}'
    date_fields = ['EXP DATE', 'REC.DATE', 'DOM']
    for field in date_fields:
        if field in test_data:
            match = re.search(date_pattern, test_data[field])
            assert match, f"Не найдена дата в поле {field}: {test_data[field]}"
    numeric_checks = {
        'Qty': r'^\d+',
        'RECEIVER#': r'\b\d+\b'
    }
    for field, pattern in numeric_checks.items():
        if field in test_data:
            value = test_data[field]
            match = re.search(pattern, value)
            assert match, f"Не найдено число в поле {field}: {value}"
            number = match.group()
            assert number.isdigit(), f"Некорректное число в поле {field}: {number}"