# focus_logger.py

from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Input


class RegularLog(App):
    """App to display key events."""

    def compose(self) -> ComposeResult:
        yield Input()
        yield Input()
        yield Input()


if __name__ == "__main__":
    app = RegularLog()
    app.run()
