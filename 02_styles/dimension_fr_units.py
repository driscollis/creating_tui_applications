# dimension_fr_units.py

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
        self.text = Static(TEXT)
        yield self.text
        self.text2 = Static(TEXT)
        yield self.text2

    def on_mount(self) -> None:
        self.text.styles.background = "red"
        self.text.styles.height = "2fr"
        self.text2.styles.background = "blue"
        self.text2.styles.height = "1fr"


if __name__ == "__main__":
    app = WidthAndHeightApp()
    app.run()
