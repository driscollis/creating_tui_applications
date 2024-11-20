# compound_widget.py

from textual.app import App, ComposeResult
from textual.widgets import Welcome


class CompoundWidget(App):

    def compose(self) -> ComposeResult:
        yield Welcome("Exit")

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = CompoundWidget()
    app.run()