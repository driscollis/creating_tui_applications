# id3_editor_v3.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Header


class ID3Editor(App):

    CSS_PATH = "id3_editor_v3.tcss"

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
        yield Button("Save Changes", id="save")


if __name__ == "__main__":
    app = ID3Editor()
    app.run()
