# calculator.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class Calculator(App):
    CSS_PATH = "calculator.tcss"

    def compose(self) -> ComposeResult:
        yield Label("0", id="solution")

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


if __name__ == "__main__":
    app = Calculator()
    app.run()
