# outline.py

from textual.app import App, ComposeResult
from textual.widgets import Static


TEXT = """"Who are you?" said the Caterpillar.

This was not an encouraging opening for a conversation. Alice replied, rather shyly,
"I—I hardly know, Sir, just at present—at least I know who I was when I got up this morning,
but I think I must have been changed several times since then."

"What do you mean by that?" said the Caterpillar, sternly. "Explain yourself!"

"I can't explain myself, I'm afraid, Sir," said Alice, "because I am not myself, you see." """


class WidthAndHeightApp(App):

    def compose(self) -> ComposeResult:
        self.widget = Static(TEXT)
        yield self.widget

    def on_mount(self) -> None:
        self.widget.styles.background = "green"
        self.widget.styles.width = 40
        self.widget.styles.height = 10
        self.widget.styles.outline = ("dashed", "red")


if __name__ == "__main__":
    app = WidthAndHeightApp()
    app.run()
