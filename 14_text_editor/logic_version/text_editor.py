# text_editor.py

from argparse import ArgumentParser, Namespace
from pathlib import Path

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Footer, Header, TextArea

from screens import SaveFileDialog, WarningScreen


class TextViewerApp(App[None]):
    CSS_PATH = "text_editor.tcss"
    BINDINGS = [
        ("ctrl+s", "save", "Save File"),
        ("ctrl+q", "quit", "Exit the application"),
        ("escape", "esc", "Exit dialog"),
    ]

    def __init__(self, cli_args: Namespace) -> None:
        super().__init__()
        self.args = cli_args
        self.current_path = Path(self.args.filepath).absolute()
        self.app_selected_directory = Path("")
        self.text_changed = False
        try:
            with open(self.current_path) as fh:
                self.data = fh.read()
        except:
            self.data = ""

    def compose(self) -> ComposeResult:
        yield Header()
        if self.current_path.suffix.lower() == ".py":
            self.text_viewer = TextArea.code_editor(self.data, language="python")
        else:
            self.text_viewer = TextArea(self.data)

        self.title = f"Editing: {self.current_path}"
        yield self.text_viewer
        yield Footer()

    def action_esc(self) -> None:
        """
        Exit a screen but not the application itself

        Works with any screen except the main one
        """
        try:
            self.app.pop_screen()
        except:
            pass

    def action_quit(self) -> None:
        """
        Keyboard shortcut action that quits the application
        """
        def confirmation_callback(result: bool) -> None:
            if result:
                return
            else:
                self.app.exit()

        if self.text_changed:
            # Alert user that file has changed and they should save
            self.push_screen(WarningScreen("Do you want to save your changes?"), confirmation_callback)
        else:
            self.app.exit()

    def action_save(self) -> None:
        """
        Keyboard shortcut action that shows the save file dialog
        """
        self.push_screen(SaveFileDialog())

    @on(DirectoryTree.DirectorySelected)
    def on_directory_selection(self, event: DirectoryTree.DirectorySelected) -> None:
        """
        Called when the DirectorySelected message is emitted from the DirectoryTree
        """
        self.app_selected_directory = event.path

    @on(TextArea.Changed)
    def on_text_changed(self) -> None:
        """
        If the user changes the file in any way, this method gets called
        """
        self.text_changed = True
        self.title = f"*Editing: {self.current_path}"

    def on_save_file_dialog_selected(self, message: SaveFileDialog.Selected) -> None:
        """
        Message handler - Called when a custom message is posted from FileBrowser

        Saves the file
        """
        self.app.pop_screen()
        self.current_path = self.app_selected_directory / message.filename
        self.log.info(f"SAVING FILE TO {self.current_path}")
        text = self.query_one(TextArea).text
        with open(self.current_path, "w") as file:
            file.write(text)
            self.text_changed = False
        self.title = f"Saved: {self.current_path}"


def get_args() -> Namespace:
    """
    Get the arguments the user passed to the application
    """
    parser = ArgumentParser()
    parser.add_argument("-f", "--filepath", nargs="?", default="default.txt")
    return parser.parse_args()


if __name__ == "__main__":
    cli_args = get_args()
    app = TextViewerApp(cli_args)
    app.run()
