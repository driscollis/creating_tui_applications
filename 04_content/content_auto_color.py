# content_auto_color.py

from textual.app import App, ComposeResult
from textual.widgets import Label

class ContentColorsApp(App):

    def compose(self) -> ComposeResult:
        yield Label("[on sienna]This is auto text on a sienna background[/]")
        yield Label("[auto on #FF0000]This is auto text on a red background[/]")
        yield Label("[auto on white]This is black text on a white background[/]")


if __name__ == "__main__":
    app = ContentColorsApp()
    app.run()