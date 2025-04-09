# content_css.py

from textual.app import App, ComposeResult
from textual.widgets import Label

class ContentCSSApp(App):

    def compose(self) -> ComposeResult:
        yield Label("[$warning on sienna]This is using CSS on a sienna background[/]")
        yield Label("[auto on $error]This is auto text on a $error background[/]")
        yield Label("[auto on $success 75%]This is black text on a $success background[/]")


if __name__ == "__main__":
    app = ContentCSSApp()
    app.run()