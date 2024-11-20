# no_bindings.py

from textual import events
from textual.app import App, ComposeResult
from textual.color import Color
from textual.widgets import Footer, Button

class NoBindingApp(App):
    def compose(self) -> ComposeResult:
        yield Footer()

    def action_add_button(self, color: str) -> None:
        button = Button(color)
        button.styles.background = Color.parse(color)
        self.mount(button)
        self.call_after_refresh(self.screen.scroll_end, animate=False)

    def action_esc(self) -> None:
        self.exit()

    def on_key(self, event: events.Key) -> None:
        if event.key == "g":
            self.action_add_button("green")
        elif event.key == "y":
            self.action_add_button("yellow")
        elif event.key == "escape":
            self.action_esc()


if __name__ == "__main__":
    app = NoBindingApp()
    app.run()