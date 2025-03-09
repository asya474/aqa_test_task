import os
from main_classes.pdf_parser import PDFParser
pdf_path = os.path.join(os.path.dirname(__file__), "test_task.pdf")
def test_parser_valid_file():
    expected = {
        'BATCH#': '1 DOM: 13.04.2022',
        'CERT SOURCE': 'wef',
        'DESCRIPTION': 'PART',
        'EXP DATE': '13.04.2022 PO: P101',
        'LOCATION': '111 CONDITION: FN',
        'PN': 'tst SN: 123123',
        'Qty': '1',
        'REC.DATE': '18.04.2022 MFG: efwfe',
        'RECEIVER#': '9 UOM: EA',
        'REMARK': 'LOT# : 1',
        'TAGGED BY': 'NOTES:'
    }
    parsed = PDFParser.parse(pdf_path)
    assert parsed == expected