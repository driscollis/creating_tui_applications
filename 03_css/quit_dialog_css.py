# quit_dialog_css.py

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Button, Label

class QuitDialog(App):
    CSS_PATH = "dialog.tcss"

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()

if __name__ == "__main__":
    app = QuitDialog()
    app.run()