# hello_styles.py

from textual.app import App


class HelloStyleApp(App):
    def on_mount(self) -> None:
        self.screen.styles.background = "darkgreen"
        self.screen.styles.border = ("dashed", "yellow")


if __name__ == "__main__":
    app = HelloStyleApp()
    app.run()
