import os
from main_classes.pdf_parser import PDFParser
pdf_path = os.path.join(os.path.dirname(__file__), "test_task.pdf")

def test_required_elements(reference_data):
    test_data = PDFParser.parse(pdf_path)
    required_fields = [
        'PN', 'DESCRIPTION', 'LOCATION',
        'RECEIVER#', 'Qty', 'EXP DATE'
    ]
    for field in required_fields:
        assert field in test_data, f"Отсутствует обязательное поле: {field}"
        assert test_data[field] == reference_data[field], \
            f"Несоответствие в поле {field}"
