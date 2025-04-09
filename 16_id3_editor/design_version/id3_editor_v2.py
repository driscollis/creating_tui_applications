# id3_editor_v2.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Header


class ID3Editor(App):

    CSS_PATH = "id3_editor_v2.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(id="number", placeholder="Track Number")
        yield Input(id="album", placeholder="Album")
        yield Input(id="artist", placeholder="Artist")
        yield Input(id='title', placeholder="Title")
        yield Button("Save Changes", id="save")


if __name__ == "__main__":
    app = ID3Editor()
    app.run()
