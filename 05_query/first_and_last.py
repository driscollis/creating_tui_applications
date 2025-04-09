# first_and_last.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class QueryApp(App):

    def compose(self) -> ComposeResult:
        yield Label("Press a button", id="label")
        yield Button("One", id="one")
        yield Button("Two", id="two")
        yield Button("Three", id="three")

    def on_button_pressed(self) -> None:
        widgets = self.query("Button")
        s = ""
        s += f"The first button: {widgets.first()}\n"
        s += f"The last button: {widgets.last()}"
        label = self.query_one("#label")
        label.update(s)


if __name__ == "__main__":
    app = QueryApp()
    app.run()
