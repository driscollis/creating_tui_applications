# number_validation.py

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widgets import Button, Label

class NumberValidationApp(App):
    CSS_PATH = "number_validation.tcss"
    number = reactive(0)

    def validate_number(self, number: int) -> int:
        """
        Validate that the number is within bounds
        """
        if number < 0:
            number = 0
        elif number > 5:
            number = 5
        return number

    def compose(self) -> ComposeResult:
        with Horizontal(id="number_buttons"):
            yield Button("Add", id="add")
            yield Button("Subtract", id="sub")
        yield Label()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add":
            self.number += 1
        else:
            self.number -= 1

        label = self.query_one(Label)
        label.update(f"Current Value: {str(self.number)}")


if __name__ == "__main__":
    app = NumberValidationApp()
    app.run()
