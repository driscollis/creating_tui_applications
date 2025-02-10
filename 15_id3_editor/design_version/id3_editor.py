# id3_editor.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Label, Header


class ID3Editor(App):

    CSS_PATH = "id3_editor.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Track Number", id="track_number")
        yield Input(id="number")
        yield Label("Album", id="album_lbl")
        yield Input(id="album")
        yield Label("Artist", id="artist_lbl")
        yield Input(id="artist")
        yield Label("Track Title", id="title_lbl")
        yield Input(id='title')
        yield Button("Save Changes", id="save")


if __name__ == "__main__":
    app = ID3Editor()
    app.run()
