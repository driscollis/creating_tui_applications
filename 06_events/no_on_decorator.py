# no_on_decorator.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class ButtonEvents(App):

    def compose(self) -> ComposeResult:
        yield Button("Toggle Dark Mode", classes="dark mode")
        yield Button("Exit", id="exit")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "exit":
            self.exit()
        elif event.button.has_class("dark", "mode"):
            self.dark = not self.dark


if __name__ == "__main__":
    app = ButtonEvents()
    app.run()