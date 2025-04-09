# table_viewer.py

import db_utility

from pathlib import Path
from textual.app import ComposeResult
from textual.widgets import DataTable, Select
from textual.widgets import TabPane


class TableViewerPane(TabPane):

    def __init__(self, db_path: Path, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db_path = db_path
        self.tables = db_utility.get_table_names(self.db_path)
        self.tables.sort()
        self.selected_row_key = None
        self.columns = None

    def compose(self) -> ComposeResult:
        yield Select.from_values(self.tables, id="table_names_select", value=self.tables[0])
        yield DataTable(id="sqlite_table_data")
