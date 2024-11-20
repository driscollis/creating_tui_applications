# query_all.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class QueryApp(App):

    def compose(self) -> ComposeResult:
        yield Label("Press a button", id="label")
        yield Button("Test", id="button")

    def on_button_pressed(self) -> None:
        widgets = self.query()
        s = ""
        for widget in widgets:
            s += f"{widget}\n"
        label = self.query_one("#label")
        label.update(s)


if __name__ == "__main__":
    app = QueryApp()
    app.run()