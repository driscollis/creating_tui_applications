# nested_containers.py

from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.containers import Horizontal, Vertical


class NestedApp(App):
    CSS_PATH = "nested.tcss"

    def compose(self) -> ComposeResult:
        yield Vertical(
            Horizontal(
                Button("One"),
                Button("Two"),
                classes="row",
            ),
            Horizontal(
                Button("Three"),
                Button("Four"),
                classes="row",
            ),
        )


if __name__ == "__main__":
    app = NestedApp()
    app.run()