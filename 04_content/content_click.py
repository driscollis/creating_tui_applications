# content_click.py

from textual.app import App, ComposeResult
from textual.widgets import Label

class ContentClick(App):

    def compose(self) -> ComposeResult:
        yield Label("Play the [on green @click=app.bell]bells[/] today!")

if __name__ == "__main__":
    app = ContentClick()
    app.run()