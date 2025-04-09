# mutable_reactive.py

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Input, Label


class ReactiveApp(App):

    numbers: reactive[list[float]] = reactive(list, recompose=True)

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter Number:", id="innum")
        if len(self.numbers) > 1:
            num_str = " + ".join([str(x) for x in self.numbers])
            total = sum([float(x) for x in self.numbers])
            yield Label(f"{num_str} = {total}")
        elif len(self.numbers) == 1:
            yield Label(f"Total: {self.numbers[0]}")
        else:
            yield Label("Total: 0")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.numbers.append(event.value)
        self.mutate_reactive(ReactiveApp.numbers)


if __name__ == "__main__":
    app = ReactiveApp()
    app.run()
