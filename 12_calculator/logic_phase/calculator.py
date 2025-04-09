# calculator.py

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class Calculator(App):
    CSS_PATH = "calculator.tcss"

    def __init__(self) -> None:
        super().__init__()
        self.solution = "0"
        self.last_button_pressed = None

    def compose(self) -> ComposeResult:
        yield Label(self.solution, id="solution")

        yield Button("7", id="seven")
        yield Button("8", id="eight")
        yield Button("9", id="nine")
        yield Button("/", id="divide")

        yield Button("4", id="four")
        yield Button("5", id="five")
        yield Button("6", id="six")
        yield Button("*", id="multiply")

        yield Button("1", id="one")
        yield Button("2", id="two")
        yield Button("3", id="three")
        yield Button("-", id="subtract")

        yield Button(".", id="decimal")
        yield Button("0", id="zero")
        yield Button("", id="empty", disabled=True)
        yield Button("+", id="add")

        yield Button("=", id="total")
        yield Button("Clear", id="clear")

    @on(Button.Pressed)
    def on_update_equation(self, event: Button.Pressed) -> None:
        operators = ["+", "-", "*", "/"]
        special_keys = ["=", "Clear"]
        current_equation = self.solution
        label = str(event.button.label)

        if label not in operators and label not in special_keys:
            if current_equation == "0":
                self.solution = f"{label}"
            else:
                self.solution = f"{current_equation}{label}"
        elif label in operators and current_equation != "0" and \
             self.last_button_pressed not in operators and label not in special_keys:
            self.solution = f"{current_equation} {label} "

        self.last_button_pressed = label
        self.query_one("#solution").update(self.solution)

    @on(Button.Pressed, "#total")
    def on_total(self, event: Button.Pressed) -> None:
        total = str(eval(self.solution))
        self.query_one("#solution").update(total)

    @on(Button.Pressed, "#clear")
    def on_clear(self, event: Button.Pressed) -> None:
        self.query_one("#solution").update("0")
        self.solution = "0"


if __name__ == "__main__":
    app = Calculator()
    app.run()
