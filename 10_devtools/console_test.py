# console_test.py

from textual.app import App, ComposeResult
from textual.widgets import Button

class DevConsoleTest(App):
    def compose(self) -> ComposeResult:
        yield Button("OK", id="ok")
        yield Button("Cancel", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ok":
            self.log.info("You pressed the OK button")
        elif event.button.id == "cancel":
            print("You pressed CANCEL!")


if __name__ == "__main__":
    app = DevConsoleTest()
    app.run()
