# csv_viewer.py

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer, TabbedContent, TabPane


class NewTab(TabPane):
    def __init__(self, title, id) -> None:
        super().__init__(title=title, id=id)

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        ROWS = [("No Data Found", "", ""), ("Press CTRL+L to load CSV file", "", "")]
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])


class ViewerApp(App):
    BINDINGS = [
        ("ctrl+l", "load", "Load CSV File"),
        ("escape", "esc", "Exit dialog"),
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent(initial="initial"):
            yield NewTab("Tab One", id="initial")
        yield Footer()


if __name__ == "__main__":
    app = ViewerApp()
    app.run()
