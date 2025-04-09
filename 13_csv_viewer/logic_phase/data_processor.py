# data_processor.py

import csv
import pathlib


def process_csv(path: pathlib.Path) -> list[str]:
    """
    Process the CSV file and turn it into a list of lists
    """
    rows = []
    with open(path, newline="") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            rows.append(row)
    return rows
