# modal_dismiss.py

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Static, Label


TEXT = """"Who are you?" said the Caterpillar.

This was not an encouraging opening for a conversation. Alice replied, rather shyly,
"I—I hardly know, Sir, just at present—at least I know who I was when I got up this morning,
but I think I must have been changed several times since then."

"What do you mean by that?" said the Caterpillar, sternly. "Explain yourself!"

"I can't explain myself, I'm afraid, Sir," said Alice, "because I am not myself, you see." """


class QuitScreen(ModalScreen[bool]):
    """Screen with a dialog to quit."""
    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.dismiss(True)
        else:
            self.dismiss(False)


class AliceApp(App):
    CSS_PATH = "modal.tcss"
    BINDINGS = [("q", "request_quit", "Quit")]

    def compose(self) -> ComposeResult:
        self.widget = Static(TEXT)
        yield self.widget

    def on_mount(self) -> None:
        self.widget.styles.background = "green"
        self.widget.styles.width = 40
        self.widget.styles.height = 10
        self.widget.styles.border = ("dashed", "red")

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""

        def quit_callback(quit: bool | None) -> None:
            if quit:
                self.exit()

        self.push_screen(QuitScreen(), quit_callback)


if __name__ == "__main__":
    app = AliceApp()
    app.run()