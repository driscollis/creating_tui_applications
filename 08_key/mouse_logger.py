# mouse_logger.py

from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog


class MouseLog(App):
    """App to display MouseMove events."""

    def compose(self) -> ComposeResult:
        self.rich_log = RichLog()
        yield self.rich_log

    def on_mouse_move(self, event: events.MouseMove) -> None:
        self.rich_log.write(event)

    def on_click(self, event: events.Click) -> None:
        self.rich_log.write(event)


if __name__ == "__main__":
    app = MouseLog()
    app.run()
