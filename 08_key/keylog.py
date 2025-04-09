# keylog.py

from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog


class KeyLog(App):
    """App to display key events."""

    def compose(self) -> ComposeResult:
        self.rich_log = RichLog()
        yield self.rich_log

    def on_key(self, event: events.Key) -> None:
        self.rich_log.write(event)


if __name__ == "__main__":
    app = KeyLog()
    app.run()
