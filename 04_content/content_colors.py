# content_colors.py

from textual.app import App, ComposeResult
from textual.widgets import Label

class ContentColorsApp(App):

    def compose(self) -> ComposeResult:
        yield Label("[#FF0000]This is red text[/]")
        yield Label("[rgba(255, 255, 0, 1)]This is yellow text[/]")
        yield Label("[cyan]A vibrant greenish-blue[/]")
        yield Label("[rgba(50, 168, 160, 0.5)]A blue green color with alpha[/]")


if __name__ == "__main__":
    app = ContentColorsApp()
    app.run()