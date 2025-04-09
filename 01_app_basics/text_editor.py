# text_editor.py

from os import system

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class TextEditorApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Open Nano", id="nano")

    @on(Button.Pressed, "#nano")
    def run_nano(self) -> None:
        with self.suspend():
            system("nano")


if __name__ == "__main__":
    TextEditorApp().run()
