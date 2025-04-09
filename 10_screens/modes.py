# modes.py

from textual import on
from textual.app import App, ComposeResult
from textual.color import Color
from textual.screen import Screen
from textual.widgets import Button, Label, Footer

class AboutScreen(Screen):
    def compose(self) -> ComposeResult:
        self.styles.background = Color(248, 3, 252, 0.5)
        yield Label("Welcome to Textual. This application is made with Python")
        yield Footer()


class EditPreferencesScreen(Screen):
    def compose(self) -> ComposeResult:
        self.styles.background = Color(64, 235, 52, 0.5)
        yield Label("Preferences Screen")
        yield Button("Edit Main", id="main")
        yield Footer()

    @on(Button.Pressed, "#main")
    def on_main(self) -> None:
        self.dismiss()

class EditScreen(Screen):
    def compose(self) -> ComposeResult:
        self.styles.background = Color(50, 168, 82, 0.5)
        yield Label("Main Edit Screen")
        yield Button("Edit Prefs", id="prefs")
        yield Footer()

    @on(Button.Pressed, "#prefs")
    def on_switch(self) -> None:
        self.app.push_screen(EditPreferencesScreen())


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("Main screen")
        yield Label("More of the main screen")
        yield Label("Textual screen opacity")
        yield Footer()


class MainAop(App):
    BINDINGS = [("m", "switch_mode('main')", "Main Screen"),
                ("e", "switch_mode('edit')", "Edit Mode"),
                ("a", "switch_mode('about')", "About Mode")]
    MODES = {
        "main": MainScreen,
        "edit": EditScreen,
        "about": AboutScreen,
    }

    def on_mount(self) -> None:
        self.switch_mode("main")


if __name__ == "__main__":
    app = MainAop()
    app.run()
