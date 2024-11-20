# context_containers.py

from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.containers import Horizontal, Vertical


class NestedApp(App):
    CSS_PATH = "nested.tcss"

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal(classes="row"):
                yield Button("One")
                yield Button("Two")
            with Horizontal(classes="row"):
                yield Button("Three")
                yield Button("Four")


if __name__ == "__main__":
    app = NestedApp()
    app.run()