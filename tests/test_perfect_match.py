import os
import pytest
pdf_path = os.path.join(os.path.dirname(__file__), "test_task.pdf")

def test_perfect_match(reference_comparator):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, "test_task.pdf")
    if not os.path.exists(pdf_path):
        pytest.fail(f"Test PDF file not found: {pdf_path}")
    report = reference_comparator.validate(pdf_path)
    assert not any(report.values()), f"Validation failed. Issues found: {report}"