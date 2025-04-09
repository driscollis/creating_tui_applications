# id3_editor.py

import eyed3
import os
import pathlib

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, DirectoryTree, Input, Label
from textual.widgets import Footer, Header



class ID3Editor(App):

    CSS_PATH = "id3_editor.tcss"

    BINDINGS = [
        ("ctrl+l", "load", "Load MP3"),
        ("ctrl+s", "save", "Save"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.current_mp3_file_path = ""

    def compose(self) -> ComposeResult:
        track_number = Input(id="number")
        track_number.border_title = "Track Number"
        album = Input(id="album")
        album.border_title = "Album"
        artist = Input(id="artist")
        artist.border_title = "Artist"
        track_title = Input(id='title')
        track_title.border_title = "Track Title"

        yield Header()
        yield track_number
        yield album
        yield artist
        yield track_title
        yield Footer()

    def action_load(self) -> None:
        self.push_screen(FileBrowser(), self.update_ui)


    def action_save(self) -> None:
        if os.path.exists(self.current_mp3_file_path):
            mp3 = eyed3.load(self.current_mp3_file_path)
            mp3.tag.album = str(self.query_one("#album", Input).value)
            mp3.tag.artist =  str(self.query_one("#artist", Input).value)
            mp3.tag.title =  str(self.query_one("#title", Input).value)
            mp3.tag.track_num = int(self.query_one("#number", Input).value)
            mp3.tag.save()
            self.push_screen(WarningScreen(f"MP3 Updated"))


    def update_ui(self, mp3_file: str) -> None:
        if os.path.exists(mp3_file):
            self.current_mp3_file_path = mp3_file
            mp3 = eyed3.load(mp3_file)
            self.query_one("#album", Input).value = mp3.tag.album
            self.query_one("#artist", Input).value = mp3.tag.artist
            self.query_one("#title", Input).value = mp3.tag.title
            self.query_one("#number", Input).value = str(mp3.tag.track_num.count)


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
        yield Vertical(
            Label(self.warning_message, id="warning_msg"),
            Button("OK", variant="primary", id="ok_warning"),
            id="warning_dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when the OK button - dismisses the screen
        """
        self.dismiss()
        event.stop()

class FileBrowser(Screen):

    def __init__(self) -> None:
        super().__init__()
        self.selected_file = pathlib.Path("")
        self.title = "Load MP3 File"

    def compose(self) -> ComposeResult:
        yield Header()
        yield DirectoryTree(f"{pathlib.Path.home()}")
        yield Button("Load MP3", variant="primary", id="load_file")
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

        if self.selected_file.suffix.lower() != ".mp3" and self.selected_file.is_file():
            self.app.push_screen(WarningScreen("ERROR: You must choose a MP3 file!"))
            return

        self.dismiss(self.selected_file)

if __name__ == "__main__":
    app = ID3Editor()
    app.run()
