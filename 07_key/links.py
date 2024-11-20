# links.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label

TEXT = """
[@click=app.set_button_background('red')]Red Button[/]
[@click=app.set_app_background('green')]Green[/]
"""

class LinkApp(App):

    def compose(self) -> ComposeResult:
        yield Label(TEXT)
        self.button = Button("Reset Colors")
        yield self.button

    def action_set_button_background(self, color: str) -> None:
        self.button.styles.background = color

    def action_set_app_background(self, color: str) -> None:
        self.screen.styles.background = color

    def on_button_pressed(self):
        self.button.styles.background = None
        self.screen.styles.background = None

if __name__ == "__main__":
    app = LinkApp()
    app.run()