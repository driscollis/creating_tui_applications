# nested_layouts.py

from textual.app import App, ComposeResult
from textual.containers import Container, HorizontalScroll, VerticalScroll
from textual.widgets import Button

class NestedLayouts(App):
    CSS_PATH = "nested_layouts.tcss"

    def compose(self) -> ComposeResult:

        with Container(id="two-column"):
            with VerticalScroll(id="left"):
                for number in range(1, 20):
                    yield Button(f"Button {number}")
            with HorizontalScroll(id="right"):
                for number in range(1, 6):
                    yield Button(f"Button {number}")

if __name__ == "__main__":
    app = NestedLayouts()
    app.run()
