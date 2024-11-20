# screen_installation.py

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class GreenScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Dismiss the screen")]

    def compose(self) -> ComposeResult:
        self.styles.background = "green"
        yield Label("Second Screen")


class MainAop(App):
    BINDINGS = [("n", "push_screen('green')", "Green Screen")]

    def compose(self) -> ComposeResult:
        yield Label("Main screen")

    def on_mount(self) -> None:
        self.install_screen(GreenScreen(), "green")


if __name__ == "__main__":
    app = MainAop()
    app.run()