# grid.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class MyGrid(App):
    CSS_PATH = "grid.tcss"

    def compose(self) -> ComposeResult:
        yield Button("One")
        yield Button("Two")
        yield Button("Three")
        yield Button("Four")


if __name__ == "__main__":
    app = MyGrid()
    app.run()
