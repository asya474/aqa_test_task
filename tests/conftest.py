import os
import pytest
from main_classes.pdf_comparator import PDFComparator
from main_classes.pdf_parser import PDFParser
pdf_path = os.path.join(os.path.dirname(__file__), "test_task.pdf")

@pytest.fixture
def reference_comparator():
    return PDFComparator("test_task.pdf")


@pytest.fixture(scope="module")
def reference_data():
    return PDFParser.parse(pdf_path)
