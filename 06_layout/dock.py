# dock.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Static


class MyGrid(App):
    CSS_PATH = "dock.tcss"

    def compose(self) -> ComposeResult:
        yield Static("Textual Sidebar", id="sidebar")
        yield Button("One")
        yield Button("Two")
        yield Button("Three")
        yield Button("Four")


if __name__ == "__main__":
    app = MyGrid()
    app.run()
