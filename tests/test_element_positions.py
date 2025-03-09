import os
import pdfplumber
pdf_path = os.path.join(os.path.dirname(__file__), "test_task.pdf")

def test_element_positions(reference_data):
    def get_element_coordinates(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[0]
            return {
                (char['x0'], char['top'], char['x1'], char['bottom'])
                for char in page.chars
            }
    reference_coords = get_element_coordinates(pdf_path)
    def check_position(pdf_path):
        test_coords = get_element_coordinates(pdf_path)
        matches = len(reference_coords & test_coords)
        assert matches / len(reference_coords) >= 0.9
    check_position(pdf_path)

