# query_buttons.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class QueryApp(App):

    def compose(self) -> ComposeResult:
        yield Label("Press a button", id="label")
        yield Button("One", id="one")
        yield Button("Two", id="two")
        yield Button("Three")

    def on_button_pressed(self) -> None:
        s = ""
        for widget in self.query("Button"):
            s += f"{widget}\n"
        label = self.query_one("#label")
        label.update(s)


if __name__ == "__main__":
    app = QueryApp()
    app.run()
