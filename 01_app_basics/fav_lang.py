# fav_lang.py

from textual.app import App, ComposeResult
from textual.widgets import Label, Button


class LanguageApp(App[str]):
    def compose(self) -> ComposeResult:
        yield Label("What is your favorite language?")
        yield Button("Python", id="python")
        yield Button("PHP", id="php")
        yield Button("JavaScript", id="javascript")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


if __name__ == "__main__":
    app = LanguageApp()
    return_code = app.run()
    print(f"Your favorite language is: {return_code}")
