# id3_editor.py

import eyed3
import os
import pathlib

from screens import WarningScreen

from textual import on
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, DirectoryTree, Input, Label
from textual.widgets import Footer, Header



class ID3Editor(Screen):

    CSS_PATH = "id3_editor.tcss"

    BINDINGS = [
        ("ctrl+s", "save", "Save"),
    ]

    def __init__(self, mp3_path) -> None:
        super().__init__()
        self.current_mp3_file_path = mp3_path

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

    def on_mount(self) -> None:
        self.update_ui()

    def action_save(self) -> None:
        if os.path.exists(self.current_mp3_file_path):
            mp3 = eyed3.load(self.current_mp3_file_path)
            mp3.tag.album = str(self.query_one("#album", Input).value)
            mp3.tag.artist =  str(self.query_one("#artist", Input).value)
            mp3.tag.title =  str(self.query_one("#title", Input).value)
            mp3.tag.track_num = int(self.query_one("#number", Input).value)
            mp3.tag.save()
            self.app.push_screen(WarningScreen(f"MP3 Updated"), self.dismiss)


    def update_ui(self) -> None:
        if os.path.exists(self.current_mp3_file_path):
            mp3 = eyed3.load(self.current_mp3_file_path)
            self.query_one("#album", Input).value = mp3.tag.album
            self.query_one("#artist", Input).value = mp3.tag.artist
            self.query_one("#title", Input).value = mp3.tag.title
            self.query_one("#number", Input).value = str(mp3.tag.track_num.count)

if __name__ == "__main__":
    app = ID3Editor()
    app.run()
