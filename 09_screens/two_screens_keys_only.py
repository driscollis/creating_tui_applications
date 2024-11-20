# two_screens_keys_only.py

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class GreenScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Dismiss the screen")]

    def compose(self) -> ComposeResult:
        self.styles.background = "green"
        yield Label("Second Screen")


class MainAop(App):
    SCREENS = {"green": GreenScreen}
    BINDINGS = [("n", "push_screen('green')", "Green Screen")]

    def compose(self) -> ComposeResult:
        yield Label("Main screen")


if __name__ == "__main__":
    app = MainAop()
    app.run()