# domquery_methods.py
import pprint

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class QueryApp(App):

    def compose(self) -> ComposeResult:
        yield Label("Press a button", id="label")
        yield Button("Get DomQuery Methods", id="one")

    def on_button_pressed(self) -> None:
        widgets = self.query("Button")
        s = ""
        s += f"{type(widgets)}\n"
        for entry in dir(widgets):
            s += f"{entry}\n"
        label = self.query_one("#label")
        label.update(s)


if __name__ == "__main__":
    app = QueryApp()
    app.run()