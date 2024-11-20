# label_alpha.py

import random

from textual.app import App, ComposeResult
from textual.color import Color
from textual.widgets import Label

COLORS = ["red", "blue", "purple", "teal", "white"]


class LabelAlphaApp(App):
    def compose(self) -> ComposeResult:
        self.labels = [Label("") for n in range(10)]
        yield from self.labels

    def on_mount(self) -> None:
        for index, widget in enumerate(self.labels, 1):
            alpha = index * 0.1
            widget.update(f"{alpha = :.1f}")
            widget.styles.background = Color(152, 96, 247, a=alpha)

    def on_key(self) -> None:
        self.screen.styles.background = random.choice(COLORS)


if __name__ == "__main__":
    app = LabelAlphaApp()
    app.run()
