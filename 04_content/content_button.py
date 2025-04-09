# content_button.py

from textual.app import App, ComposeResult
from textual.widgets import Label, Button

class ContentButton(App):

    def compose(self) -> ComposeResult:
        yield Label("Play the [on green @click=app.bell]bells[/] today!")
        yield Button("[red]Red[/] [green]Green[/]")


if __name__ == "__main__":
    app = ContentButton()
    app.run()