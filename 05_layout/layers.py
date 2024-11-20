# layers.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class LayeredApp(App):
    CSS_PATH = "layers.tcss"

    def compose(self) -> ComposeResult:
        yield Button("One", id="btn_one")
        yield Button("Two", id="btn_two")


if __name__ == "__main__":
    app = LayeredApp()
    app.run()