# content_test.py

from textual.app import App, ComposeResult
from textual.widgets import Label

class ContentTest(App):

    def compose(self) -> ComposeResult:
        yield Label("[red][italic]Textual[/italic][/] Rocks!")
        yield Label("[green]Python[/] for the win!")


if __name__ == "__main__":
    app = ContentTest()
    app.run()