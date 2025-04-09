# data_processor.py

import csv
import io
import pathlib
import pandas as pd


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


def process_excel(path: pathlib.Path) -> list[str]:
    """
    Process an Excel file using Pandas
    """
    f_obj = io.StringIO()
    df = pd.read_excel(path)
    df.to_csv(f_obj)
    f_obj.seek(0)

    rows = []
    reader = csv.reader(f_obj)
    for row in reader:
        rows.append(row)
    return rows
