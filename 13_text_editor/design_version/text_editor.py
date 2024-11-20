# text_editor.py

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, TextArea


class TextViewerApp(App[None]):
    BINDINGS = [
        ("ctrl+s", "save", "Save File"),
        ("ctrl+q", "quit", "Exit the application"),
        ("escape", "esc", "Exit dialog"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        self.text_viewer = TextArea("")
        yield self.text_viewer
        yield Footer()


if __name__ == "__main__":
    app = TextViewerApp()
    app.run()