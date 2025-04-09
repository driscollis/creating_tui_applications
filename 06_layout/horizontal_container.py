# horizontal_container.py

from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.containers import Horizontal


class HorizontalApp(App):

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("OK"),
            Button("Cancel"),
            Button("Go!"),
        )


if __name__ == "__main__":
    app = HorizontalApp()
    app.run()
