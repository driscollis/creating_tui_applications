# query_one_same_ids.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class QueryApp(App):

    def compose(self) -> ComposeResult:
        yield Label("Press a button", id="label")
        yield Button("Test", id="button")

    def on_button_pressed(self) -> None:
        widget = self.query_one("#label")
        widget.update("You pressed the button!")


if __name__ == "__main__":
    app = QueryApp()
    app.run()