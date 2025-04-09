# screenshot.py

from textual.app import App, ComposeResult
from textual.widgets import Button

class ScreenshotApp(App):
    def compose(self) -> ComposeResult:
        yield Button("Take Screenshot")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.save_screenshot(filename="textual_screenshot.svg")

if __name__ == "__main__":
    app = ScreenshotApp()
    app.run()
