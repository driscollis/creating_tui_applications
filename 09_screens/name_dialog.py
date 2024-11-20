# name_dialog.py

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Static, Label, Input


TEXT = """"Who are you?" said the Caterpillar.

This was not an encouraging opening for a conversation. Alice replied, rather shyly,
"I—I hardly know, Sir, just at present—at least I know who I was when I got up this morning,
but I think I must have been changed several times since then."

"What do you mean by that?" said the Caterpillar, sternly. "Explain yourself!"

"I can't explain myself, I'm afraid, Sir," said Alice, "because I am not myself, you see." """


class NameScreen(ModalScreen):
    """Screen with a dialog to quit."""
    def compose(self) -> ComposeResult:
        yield Grid(
            Input(placeholder="What is your name?", id="question"),
            Button("OK", variant="error", id="ok"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ok":
            name = self.query_one(Input).value
            self.dismiss(name)
        else:
            self.dismiss(False)


class AliceApp(App):
    CSS_PATH = "name.tcss"
    BINDINGS = [("n", "request_name", "Get name")]

    def compose(self) -> ComposeResult:
        self.widget = Static(TEXT)
        yield self.widget

    def on_mount(self) -> None:
        self.widget.styles.background = "green"
        self.widget.styles.width = 40
        self.widget.styles.height = 10
        self.widget.styles.border = ("dashed", "red")

    def action_request_name(self) -> None:
        """Action to display the name dialog."""

        def ok_callback(name: bool | str| None) -> None:
            if isinstance(name, str):
                self.query_one(Static).update(f"Hello {name}")

        self.push_screen(NameScreen(), ok_callback)


if __name__ == "__main__":
    app = AliceApp()
    app.run()