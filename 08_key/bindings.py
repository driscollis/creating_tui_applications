# bindings.py

from textual.app import App, ComposeResult
from textual.color import Color
from textual.widgets import Footer, Button


class BindingApp(App):
    BINDINGS = [
        ("g", "add_button('green')", "Add green button"),
        ("y", "add_button('yellow')", "Add yellow button"),
        ("escape", "esc", "Exit application")
    ]

    def compose(self) -> ComposeResult:
        yield Footer()

    async def action_add_button(self, color: str) -> None:
        button = Button(color)
        button.styles.background = Color.parse(color)
        await self.mount(button)
        self.call_after_refresh(self.screen.scroll_end, animate=False)

    def action_esc(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = BindingApp()
    app.run()
