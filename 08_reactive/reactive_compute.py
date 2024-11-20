# reactive_compute.py

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Input, Label


class ReactiveApp(App):

    first = reactive(0.0)
    second = reactive(0.0)
    total = reactive(0.0)

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter Number One:", id="one")
        yield Input(placeholder="Enter Number Two:", id="two")
        yield Label("Total: 0")

    def compute_total(self) -> float:
        return self.first + self.second

    def watch_total(self, number: float) -> None:
        self.query_one(Label).update(f"Total: {number}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        try:
            number = float(event.value)
        except ValueError:
            return

        if event.input.id == "one":
            self.first = number
        elif event.input.id == "two":
            self.second = number

if __name__ == "__main__":
    app = ReactiveApp()
    app.run()
