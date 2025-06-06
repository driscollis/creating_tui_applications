# db_utility.py

import sqlite3

from sqlalchemy import create_engine
from sqlalchemy import inspect


def get_table_names(db_path: str) -> list[str]:
    engine = create_engine(fr"sqlite:///{db_path}")
    insp = inspect(engine)
    return insp.get_table_names()


def get_data_from_table(db_path: str, table_name: str) -> list[tuple]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    sql = f"SELECT * FROM {table_name} LIMIT 1000;"
    cursor.execute(sql)

    # Get column names
    column_names = tuple([description[0] for description in cursor.description])

    data = cursor.fetchall()
    data.insert(0, column_names)
    return data

def get_schema(db_path: str) -> dict[str, dict]:
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


def run_sql(db_path: str, sql: str) -> list[tuple]:
    """
    Runs the user provided SQL. This may be a select, update, drop
    or any other SQL command

    If there are results, they will be returned
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    headers = [name[0] for name in cursor.description]
    result = cursor.fetchall()
    result.insert(0, tuple(headers))
    conn.commit()
    return result
