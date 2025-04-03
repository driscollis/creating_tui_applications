# setup_screen.py

import pathlib

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Header, Input


class SetupScreen(ModalScreen):

    CSS_PATH = "setup_screen.tcss"

    BINDINGS = [("escape", "exit_screen", "Exit")]

    def __init__(self, smtp_config: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.smtp_config = pathlib.Path(smtp_config)

    def compose(self) -> ComposeResult:
        self.smtp_server = Input(id="server")
        self.smtp_server.border_title = "SMTP Server"
        self.port = Input(id="port")
        self.port.border_title = "SMTP Port"
        self.username = Input(id="username")
        self.username.border_title = "Username"

        yield Vertical(
            Header(),
            self.smtp_server,
            self.port,
            self.username,
            Horizontal(
                Button("Save", variant="primary", id="save_smtp"),
                Button("Cancel", variant="error", id="cancel_smtp")
            ),
            id="smtp_dialog"
        )
