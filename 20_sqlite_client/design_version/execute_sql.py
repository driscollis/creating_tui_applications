# execute_sql.py

from pathlib import Path
from textual.app import ComposeResult
from textual.widgets import Button, DataTable, TextArea, RichLog
from textual.widgets import TabPane


class ExecuteSQLPane(TabPane):

    def __init__(self, db_path: Path, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db_path = db_path

    def compose(self) -> ComposeResult:
        text = TextArea(id="sql_commands")
        text.border_title = "SQL"
        results = DataTable(id="sql_results_table", zebra_stripes=True)
        results.border_title = "SQL Results"
        sql_command_output = RichLog(id="sql_log")
        sql_command_output.border_title = "SQL Output / Status"
        yield text
        yield Button("Run SQL", id="run_sql_btn", variant="primary")
        yield results
        yield sql_command_output

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        data = [("No", "Data", "Loaded"), ("", "", "")]
        table.add_columns(*data[0])
        table.add_rows(data[1:])
        table.cursor_type = "row"
