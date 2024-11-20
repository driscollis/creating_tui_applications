# opacity.py

from textual.app import App, ComposeResult
from textual.color import Color
from textual.screen import Screen
from textual.widgets import Label


class GreenScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Dismiss the screen")]

    def compose(self) -> ComposeResult:
        self.styles.background = Color(50, 168, 82, 0.5)
        yield Label("Second Screen")


class MainAop(App):
    BINDINGS = [("n", "push_screen('green')", "Green Screen")]

    def compose(self) -> ComposeResult:
        yield Label("Main screen")
        yield Label("More of the main screen")
        yield Label("Textual screen opacity")

    def on_mount(self) -> None:
        self.install_screen(GreenScreen(), "green")


if __name__ == "__main__":
    app = MainAop()
    app.run()
