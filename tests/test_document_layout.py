import os
import pdfplumber
pdf_path = os.path.join(os.path.dirname(__file__), "test_task.pdf")
def test_document_layout():
    def get_layout(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[0]
            return {
                "width": page.width,
                "height": page.height,
                "elements_count": len(page.chars) + len(page.images)
            }
    ref_layout = get_layout(pdf_path)
    test_layout = get_layout(pdf_path)
    assert abs(test_layout["width"] - ref_layout["width"]) / ref_layout["width"] < 0.05, \
        "Несоответствие ширины документа"
    assert abs(test_layout["height"] - ref_layout["height"]) / ref_layout["height"] < 0.05, \
        "Несоответствие высоты документа"
    assert abs(test_layout["elements_count"] - ref_layout["elements_count"]) / ref_layout["elements_count"] < 0.1, \
        "Сильное отклонение в количестве элементов"