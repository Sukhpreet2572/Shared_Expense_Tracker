import csv

from .anomaly_detector import AnomalyDetector


class CSVImportService:

    def read_csv(self, file_path):

        with open(file_path, 'r', encoding='utf-8') as file:

            rows = list(csv.DictReader(file))

        detector = AnomalyDetector()

        for row in rows:

            row["anomalies"] = detector.detect(row)

            if detector.is_duplicate(row, rows):
                row["anomalies"].append("DUPLICATE_EXPENSE")

        return rows