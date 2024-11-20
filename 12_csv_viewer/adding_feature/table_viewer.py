# table_viewer.py

import data_processor
import pathlib
from screens import FileBrowser

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, DataTable, DirectoryTree, Footer
from textual.widgets import Label, TabbedContent, TabPane


class NewTab(TabPane):
    def __init__(self, data, title, id) -> None:
        super().__init__(title=title, id=id)
        self.data = data

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.clear(columns=True)
        table.add_columns(*self.data[0])
        table.add_rows(self.data[1:])
        table.cursor_type = "row"


class ViewerApp(App):
    CSS_PATH = "csv_viewer.tcss"
    BINDINGS = [
        ("ctrl+l", "load", "Load CSV File"),
        ("escape", "esc", "Exit dialog"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.app_selected_file = pathlib.Path("")

    def compose(self) -> ComposeResult:
        yield Footer()

        with TabbedContent(initial="initial"):
            with TabPane("Load CSV", id="initial"):
                yield Label("Choose a CSV file to load:")
                yield Button("Load")

    def action_esc(self) -> None:
        """
        Exit a screen but not the application itself

        Works with any screen except the main one
        """
        try:
            self.app.pop_screen()
        except:
            pass

    def action_load(self) -> None:
        """
        Action called with ctrl+L - shows file browser
        """
        self.push_screen(FileBrowser())

    def on_button_pressed(self) -> None:
        """
        Show file browser
        """
        self.push_screen(FileBrowser())

    @on(DirectoryTree.FileSelected)
    def on_file_selection(self, event: DirectoryTree.FileSelected) -> None:
        """
        Called when the FileSelected message is emitted from the DirectoryTree
        """
        self.app_selected_file = event.path

    def on_file_browser_selected(self, message: FileBrowser.Selected) -> None:
        """
        Message handler - Called when a custom message is posted from FileBrowser
        """
        self.app.pop_screen()

        # Parse the file
        if self.app_selected_file.suffix.lower() == ".csv":
            rows = data_processor.process_csv(self.app_selected_file)
        elif self.app_selected_file.suffix.lower() == ".xlsx":
            rows = data_processor.process_excel(self.app_selected_file)

        # Load the DataTable
        tab_mgr = self.query_one(TabbedContent)
        tab_id = f"{self.app_selected_file.stem}"
        new_tab = NewTab(rows, title=f"{self.app_selected_file.name}", id=tab_id)
        tab_mgr.add_pane(new_tab)
        tab_mgr.active = tab_id


if __name__ == "__main__":
    app = ViewerApp()
    app.run()
