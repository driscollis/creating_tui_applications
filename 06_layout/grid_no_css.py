# grid_no_css.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class FakeGrid(App):

    def compose(self) -> ComposeResult:
        yield Button("One")
        yield Button("Two")
        yield Button("Three")
        yield Button("Four")


if __name__ == "__main__":
    app = FakeGrid()
    app.run()
