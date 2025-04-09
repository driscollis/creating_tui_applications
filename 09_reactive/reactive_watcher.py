# reactive_watcher.py

from textual.app import App, ComposeResult
from textual.color import Color, ColorParseError
from textual.reactive import reactive
from textual.widgets import Input, Button


class ReactiveApp(App):

    color = reactive(Color.parse("transparent"))

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter color:")
        yield Button("No color selected")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        try:
            input_color = Color.parse(event.value)
        except ColorParseError:
            pass
        else:
            # Reset the input
            self.query_one(Input).value = ""
            # Update label
            self.query_one(Button).label = f"You chose: '{input_color}'"
            self.color = input_color

    def watch_color(self, old, new):
        word = self.query_one(Button)
        inpt = self.query_one(Input)
        inpt.styles.background = old
        word.styles.background = new


if __name__ == "__main__":
    app = ReactiveApp()
    app.run()
