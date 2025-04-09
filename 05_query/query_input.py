# query_input.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Input


class QueryInput(App):

    def compose(self) -> ComposeResult:
        yield Input()
        yield Button("Update Input")

    def on_button_pressed(self) -> None:
        input_widget = self.query_one(Input)
        new_string = f"You entered: {input_widget.value}"
        input_widget.value = new_string


if __name__ == "__main__":
    app = QueryInput()
    app.run()
