# widget_colors.py

from textual.app import App, ComposeResult
from textual.color import Color
from textual.widgets import Button, Label, Static


class WidgetColorApp(App):
    def compose(self) -> ComposeResult:
        self.static = Static("Static text")
        yield self.static
        self.button = Button("Exit")
        yield self.button
        self.label = Label("Label")
        yield self.label

    def on_mount(self) -> None:
        self.static.styles.background = "#8F888F"
        self.button.styles.background = "hsl(250,42.9%,49.4%)"
        self.label.styles.color = "green"
        self.label.styles.background = Color(242, 247, 96)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit()


if __name__ == "__main__":
    app = WidgetColorApp()
    app.run()
