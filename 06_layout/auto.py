# auto.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class MyGrid(App):
    CSS_PATH = "auto.tcss"

    def compose(self) -> ComposeResult:
        yield Button("A Stupidly Long Label For A Button")
        yield Button("Two")
        yield Button("Three")
        yield Button("Four")


if __name__ == "__main__":
    app = MyGrid()
    app.run()
