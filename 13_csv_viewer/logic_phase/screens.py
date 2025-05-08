# screens.py

import pathlib

from textual import on
from textual.app import ComposeResult
from textual.containers import Grid
from textual.message import Message
from textual.screen import Screen
from textual.widgets import Button, DirectoryTree, Footer, Label


class WarningScreen(Screen):
    """
    Creates a pop-up Screen that displays a warning message to the user
    """

    def __init__(self, warning_message: str) -> None:
        super().__init__()
        self.warning_message = warning_message

    def compose(self) -> ComposeResult:
        """
        Create the UI in the Warning Screen
        """
        yield Grid(
            Label(self.warning_message, id="warning_msg"),
            Button("OK", variant="primary", id="ok_warning"),
            id="warning_dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when the OK button - dismisses the screen
        """
        self.app.pop_screen()
        event.stop()


class FileBrowser(Screen):
    class Selected(Message):
        """
        File selected message
        """

        def __init__(self, attr: str) -> None:
            self.attr = attr
            super().__init__()

    def __init__(self) -> None:
        super().__init__()
        self.selected_file = pathlib.Path("")

    def compose(self) -> ComposeResult:
        yield Label("Load CSV File")
        yield DirectoryTree("/")
        yield Button("Load File", variant="primary", id="load_file")
        yield Footer()

    @on(DirectoryTree.FileSelected)
    def on_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        """
        Called when the FileSelected Message is emitted from the DirectoryTree
        """
        self.selected_file = event.path

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when the load file button is pressed
        """
        event.stop()

        if self.selected_file.suffix.lower() != ".csv":
            self.app.push_screen(WarningScreen("ERROR: You must choose a CSV file!"))
            return

        self.post_message(self.Selected("selected"))
        self.dismiss()
