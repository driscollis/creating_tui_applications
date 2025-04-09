# compose_email.py

import pathlib
import utility

from smtplib import SMTPRecipientsRefused
from textual import on
from textual.app import ComposeResult
from textual.containers import Center, Grid, Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Header, Input, Label, TextArea

from address_book import AddressBook


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


class PasswordScreen(ModalScreen):

    DEFAULT_CSS = """
        TextEntryDialog {
            align: center middle;
            background: $primary-lighten-1 30%;
        }

        #text-entry-dlg {
            width: 80;
            height: 14;
            border: thick $background 70%;
            content-align: center middle;
            margin: 1;
        }

        #text-entry-label {
            margin: 1;
        }

        Button {
            width: 50%;
            margin: 1;
        }
        """

    def compose(self) -> ComposeResult:
        yield Vertical(
            Header(),
            Center(Label("Enter your email password", id="text-entry-label")),
            Input(placeholder="", id="answer", password=True),
            Center(
                Horizontal(
                    Button("OK", variant="primary", id="text-entry-ok"),
                    Button("Cancel", variant="error", id="text-entry-cancel"),
                )
            ),
            id="text-entry-dlg",
        )

    @on(Button.Pressed, "#text-entry-ok")
    def on_ok(self, event: Button.Pressed) -> None:
        """
        Return the user's entry back to the calling application and dismiss the dialog
        """
        answer = self.query_one("#answer").value
        self.dismiss(answer)

    @on(Button.Pressed, "#text-entry-cancel")
    def on_cancel(self, event: Button.Pressed) -> None:
        """
        Returns an empty string to the calling application and dismisses the dialog
        """
        self.dismiss("")


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

    def action_exit_screen(self) -> None:
        self.dismiss()

    def action_get_email(self) -> None:
        self.app.push_screen(AddressBook(get_address=True), self.add_email)

    @on(Button.Pressed, "#send")
    def on_send_email(self) -> None:
        if not self.to_addresses.value:
            self.app.push_screen(WarningScreen("You must enter a valid email!"))
            return

        if not self.email_subject.value:
            self.app.push_screen(WarningScreen("You must enter a valid subject line!"))
            return

        if not self.email_body.text:
            self.app.push_screen(WarningScreen("You must enter some text to email!"))
            return

        if not pathlib.Path("smtp.ini").exists():
            self.app.push_screen(WarningScreen(
                "SMTP Server Settings not set. Go back home and configure it!"))
            return

        try:
            utility.send_email(self.smtp_config, self.to_addresses.value, self.email_subject.value, self.email_body.text)
        except SMTPRecipientsRefused:
            # SMTP server requires authentication
            self.app.push_screen(PasswordScreen(), self.send_email_with_password)
        self.dismiss()

    def send_email_with_password(self, password: str = "") -> None:
        if password:
            utility.send_email_with_password(
                self.smtp_config, self.to_addresses.value, self.email_subject.value, self.email_body.text, password)

    def add_email(self, email: str) -> None:
        if email:
            current_email = self.to_addresses.value

            if current_email:
                self.to_addresses.value = f"{current_email},{email}"
            else:
                self.to_addresses.value = email