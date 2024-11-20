# two_screens.py

from textual import on
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Button

class GreenScreen(Screen):

    def compose(self) -> ComposeResult:
        self.styles.background = "green"
        yield Button("Main Screen", id="main")

    @on(Button.Pressed, "#main")
    def on_main(self) -> None:
        self.dismiss()


class MainAop(App):

    def compose(self) -> ComposeResult:
        yield Button("Switch", id="switch")

    @on(Button.Pressed, "#switch")
    def on_switch(self) -> None:
        self.push_screen(GreenScreen())


if __name__ == "__main__":
    app = MainAop()
    app.run()