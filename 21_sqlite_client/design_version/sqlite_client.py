# sqlite_client_v3.py

from pathlib import Path
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Button, Footer, Header, Input
from textual.widgets import Label, TabbedContent, TabPane

from database_structure_tree import DatabaseStructurePane
from execute_sql import ExecuteSQLPane
from table_viewer import TableViewerPane


class SQLiteClientApp(App):

    BINDINGS = [
        ("o", "open_database", "Open Database"),
        ("q", "quit", "Exit the program"),
        ("f5", "run_sql", "Run SQL"),
    ]

    CSS_PATH = "sqlite_client.tcss"

    def __init__(self, cli_args: Namespace, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = cli_args
        self.title = "Squall"
        self.execute_sql_pane = None

    def compose(self) -> ComposeResult:
        db_path = Input(id="db_path_input")
        db_path.border_title = "Database Path"
        yield Header()
        yield Center(
            Button("Open Database", id="open_db_btn", variant="primary"),
            id="center"
            )
        with TabbedContent("Database", id="tabbed_ui"):
            with TabPane("Database Structure"):
                yield Label("No data loaded")
            with TabPane("Table Viewer"):
                yield Label("No data loaded")
            with TabPane("Execute SQL"):
                yield Label("No data loaded")
        yield Footer()


if __name__ == "__main__":
    app = SQLiteClientApp()
    app.run()
