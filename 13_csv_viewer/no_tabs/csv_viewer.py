# csv_viewer.py

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer


class ViewerApp(App):
    BINDINGS = [
        ("ctrl+l", "load", "Load CSV File"),
        ("escape", "esc", "Exit dialog"),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        ROWS = [("No Data Found", "", ""), ("Press CTRL+L to load CSV file", "", "")]
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])


if __name__ == "__main__":
    app = ViewerApp()
    app.run()
