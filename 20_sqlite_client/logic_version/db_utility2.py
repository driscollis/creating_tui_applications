# db_utility.py

from sqlalchemy import create_engine
from sqlalchemy import inspect

def parse_db(db_path: str):
    engine = create_engine(fr"sqlite:///{db_path}")
    insp = inspect(engine)

    tables = insp.get_table_names()

    table_data = {}
    for table in tables:
        columns = insp.get_columns(table)
        column_data = {}
        for column in columns:
            column_name = column["name"]
            column_type = str(column["type"])
            column_data[column_name] = {}
            column_data[column_name]["Type"] = column_type
            column_data[column_name]["Schema"] = column
        table_data[table] = {}
        table_data[table]["Columns"] = column_data

    return table_data


pim = r"C:\Users\wheifrd\.local\share\pim\game_data.sqlite"
parse_db(pim)