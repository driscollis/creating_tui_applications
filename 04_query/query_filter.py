# query_filter.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class QueryApp(App):

    def compose(self) -> ComposeResult:
        yield Label("Press a button", id="label")
        yield Button("One", id="one")
        yield Button("Two", id="two")
        yield Button("Three", id="three")

    def on_button_pressed(self) -> None:
        widgets = self.query()
        label_widget = widgets.filter("Label")
        s = ""
        s += f"{label_widget}"
        label = self.query_one("#label")
        label.update(s)


if __name__ == "__main__":
    app = QueryApp()
    app.run()