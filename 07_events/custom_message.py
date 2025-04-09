# custom_message.py

import pathlib

from textual import on
from textual.app import App, ComposeResult
from textual.message import Message
from textual.screen import Screen
from textual.widgets import Button, DirectoryTree, Input, Label


class FileBrowser(Screen):
    class Selected(Message):
        """
        File selected message
        """

        def __init__(self, path: str) -> None:
            self.path = path
            super().__init__()

    def __init__(self) -> None:
        super().__init__()
        self.selected_file = pathlib.Path("")

    def compose(self) -> ComposeResult:
        yield Label("Load a File")
        yield DirectoryTree("c:/")
        yield Button("Load File")

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
        self.post_message(self.Selected(str(self.selected_file)))


class FileApp(App):
    def compose(self) -> ComposeResult:
        self.input = Input("No File Selected")
        yield self.input
        yield Button("Choose File")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.push_screen(FileBrowser())

    def on_file_browser_selected(self, message: FileBrowser.Selected) -> None:
        """
        Message handler - Called when a custom message is posted from FileBrowser
        """
        self.app.pop_screen()
        self.input.value = message.path


if __name__ == "__main__":
    app = FileApp()
    app.run()
