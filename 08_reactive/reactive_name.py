# reactive_name.py

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Input, Label

class Word(Label):
    """
    Create a greeting in a label
    """

    name = reactive("name")

    def render(self) -> str:
        return f"Greetings, {self.name}!"


class ReactiveApp(App):

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter name or word:")
        yield Word()

    def on_input_changed(self, event: Input.Changed) -> None:
        word = self.query_one(Word)
        word.name = event.value

if __name__ == "__main__":
    app = ReactiveApp()
    app.run()
