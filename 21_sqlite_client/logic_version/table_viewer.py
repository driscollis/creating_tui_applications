# table_viewer.py

import db_utility
import sqlite3

from pathlib import Path
from textual import on
from textual.app import ComposeResult
from textual.widgets import DataTable, Select
from textual.widgets import TabPane


class TableViewerPane(TabPane):

    def __init__(self, db_path: Path, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db_path = db_path
        self.tables = db_utility.get_table_names(self.db_path)
        self.tables.sort()
        self.columns = None

    def compose(self) -> ComposeResult:
        yield Select.from_values(self.tables, id="table_names_select", value=self.tables[0])
        yield DataTable(id="sqlite_table_data")

    def on_mount(self) -> None:
        self.update_sqlite_table_view()

    @on(Select.Changed, "#table_names_select")
    def update_sqlite_table_view(self) -> None:
        current_table = self.app.query_one("#table_names_select").value

        try:
            data = db_utility.get_data_from_table(self.db_path, current_table)
        except sqlite3.OperationalError:
            return

        self.columns = data[0]
        table = self.query_one(DataTable)
        table.clear(columns=True)
        table.add_columns(*self.columns)
        if len(data[1:]):
            table.add_rows(data[1:])
        else:
            table.add_rows([tuple(["" for x in data[0]])])

        table.cursor_type = "row"
