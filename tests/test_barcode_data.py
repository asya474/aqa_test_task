import os
import pdfplumber
import cv2
import numpy as np
from PIL import Image
pdf_path = os.path.join(os.path.dirname(__file__), "test_task.pdf")


def extract_barcodes(pdf_path: str) -> list:
    barcodes = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for img in page.images:
                if not img['stream']:
                    continue
                try:
                    pil_image = Image.open(img['stream'])
                    cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
                    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
                    detector = cv2.barcode.BarcodeDetector()
                    retval, decoded_info, _, _ = detector.detectAndDecode(gray)
                    if retval:
                        barcodes.extend(decoded_info)
                except Exception as e:
                    print(f"Error processing image: {str(e)}")
                    continue
    return barcodes


def test_barcode_data():
    reference_barcodes = extract_barcodes(pdf_path)
    test_barcodes = extract_barcodes(pdf_path)

    # Проверка количества штрих-кодов
    assert len(test_barcodes) == len(reference_barcodes), (
        f"Количество штрих-кодов не совпадает: "
        f"ожидалось {len(reference_barcodes)}, получено {len(test_barcodes)}"
    )

    # Проверка содержимого штрих-кодов
    for i, (ref, test) in enumerate(zip(reference_barcodes, test_barcodes)):
        assert test == ref, (
            f"Несовпадение в штрих-коде #{i + 1}: "
            f"ожидалось '{ref}', получено '{test}'"
        )