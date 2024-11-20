# on_decorator.py

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class ButtonEvents(App):

    def compose(self) -> ComposeResult:
        yield Button("Toggle Dark Mode", classes="dark mode")
        yield Button("Exit", id="exit")

    @on(Button.Pressed, ".dark.mode")
    def toggle_dark_mode(self) -> None:
        """
        Called when the "Toggle Dark Mode" button is pressed
        """
        self.dark = not self.dark

    @on(Button.Pressed, "#exit")
    def quit_app(self):
        """
        Called when the "Exit" button is pressed
        """
        self.exit()

if __name__ == "__main__":
    app = ButtonEvents()
    app.run()