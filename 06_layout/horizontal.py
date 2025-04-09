# horizontal.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class HorizontalApp(App):
    CSS_PATH = "horizontal.tcss"

    def compose(self) -> ComposeResult:
        yield Button("OK")
        yield Button("Cancel")
        yield Button("Go!")


if __name__ == "__main__":
    app = HorizontalApp()
    app.run()
