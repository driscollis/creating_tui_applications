# verical.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class VerticalApp(App):

    def compose(self) -> ComposeResult:
        yield Button("OK")
        yield Button("Cancel")
        yield Button("Go!")


if __name__ == "__main__":
    app = VerticalApp()
    app.run()
