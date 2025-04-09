# content_opacity.py

from textual.app import App, ComposeResult
from textual.widgets import Label

class ContentColorsApp(App):

    def compose(self) -> ComposeResult:
        yield Label("[on sienna 50%]This is auto text on a sienna background[/]")
        yield Label("[auto on #FF0000 25%]This is auto text on a red background[/]")
        yield Label("[auto on white 75%]This is black text on a white background[/]")


if __name__ == "__main__":
    app = ContentColorsApp()
    app.run()