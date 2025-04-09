# smtp_client_tui.py

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, OptionList
from textual.widgets.option_list import Option

from address_book import AddressBook
from compose_email import ComposeEmailScreen
from setup_screen import SetupScreen


class SMTPClientApp(App):

    BINDINGS = [
        ("a", "address_book", "Address Book"),
        ("c", "compose_email", "Compose"),
        ("s", "setup", "Setup SMTP Client"),
        ("q", "quit", "Exit the program"),
    ]

    def __init__(self, driver_class=None, css_path=None, watch_css=False, ansi_color=False):
        super().__init__(driver_class, css_path, watch_css, ansi_color)
        self.smtp_config = "smtp.ini"

    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(id="main_menu")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "SMTP TUI"
        menu_items = ["[cyan]A[/cyan]   Address Book      - Update address book",
                      "[cyan]C[/cyan]   Compose Message   - Compose and send a message",
                      "[cyan]S[/cyan]   Setup             - Setup SMTP Client",
                      "[cyan]Q[/cyan]   Quit              - Exit the program",
                      ]
        main_menu = self.query_one("#main_menu", OptionList)
        for item in menu_items:
            main_menu.add_option(Option(item))
            # Add a separator using None (v2.0.0+)
            main_menu.add_option(None)

    def action_setup(self) -> None:
        """
        Open the setup screen
        """
        self.push_screen(SetupScreen(self.smtp_config))

    def action_compose_email(self) -> None:
        """
        Compose and send an email
        """
        self.push_screen(ComposeEmailScreen(self.smtp_config))

    def action_address_book(self) -> None:
        self.push_screen(AddressBook())


if __name__ == "__main__":
    app = SMTPClientApp()
    app.run()
