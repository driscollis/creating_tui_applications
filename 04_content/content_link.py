# content_link.py

from textual.app import App, ComposeResult
from textual.widgets import Label

class ContentLink(App):

    def compose(self) -> ComposeResult:
        yield Label(
            "[green link='https://www.blog.pythonlibrary.org/']"
            "Visit Mouse vs Python[/] today!"
        )


if __name__ == "__main__":
    app = ContentLink()
    app.run()