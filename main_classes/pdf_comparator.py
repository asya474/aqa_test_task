from main_classes.pdf_parser import PDFParser


class PDFComparator:
    def __init__(self, reference_path: str):
        self.reference = PDFParser.parse(reference_path)
        self.required_keys = set(self.reference.keys())
    def validate(self, test_path: str) -> dict:
        test_data = PDFParser.parse(test_path)
        report = {
            "missing_keys": [],
            "extra_keys": [],
            "value_mismatches": [],
        }
        test_keys = set(test_data.keys())
        report["missing_keys"] = list(self.required_keys - test_keys)
        report["extra_keys"] = list(test_keys - self.required_keys)
        for key in self.required_keys & test_keys:
            if self.reference[key] != test_data[key]:
                report["value_mismatches"].append({
                    "key": key,
                    "expected": self.reference[key],
                    "actual": test_data[key]
                })
        return report
