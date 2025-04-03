# compose_email.py

import pathlib

from textual.app import ComposeResult
from textual.containers import Grid, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Header, Input, Label, TextArea


class WarningScreen(ModalScreen):
    """
    Creates a pop-up Screen that displays a warning message to the user
    """

    def __init__(self, warning_message: str) -> None:
        super().__init__()
        self.warning_message = warning_message

    def compose(self) -> ComposeResult:
        """
        Create the UI in the Warning Screen
        """
        yield Grid(
            Label(self.warning_message, id="warning_msg"),
            Button("OK", variant="primary", id="ok_warning"),
            id="warning_dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when the OK button - dismisses the screen
        """
        self.dismiss()
        event.stop()


class ComposeEmailScreen(ModalScreen):

    CSS_PATH = "compose_email.tcss"
    BINDINGS = [
        ("escape", "exit_screen", "Exit"),
        ("f2", "get_email", "Open Address Book"),
    ]

    def __init__(self, smtp_config: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.smtp_config = pathlib.Path(smtp_config)
        self.title = "Compose Email"

    def compose(self) -> ComposeResult:
        self.to_addresses = Input(id="to_addesses")
        self.to_addresses.border_title = "TO:"

        self.email_subject = Input(id="email_subject")
        self.email_subject.border_title = "Email Subject:"

        self.email_body = TextArea(id="email_text")
        self.email_body.border_title = "Email Body"

        yield Header()
        yield Vertical(
            self.to_addresses,
            self.email_subject,
            self.email_body,
            Button("Send", id="send", variant="primary"),
            id="compose_email_dlg"
        )
        yield Footer()
