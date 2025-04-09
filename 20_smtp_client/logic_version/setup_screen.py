# setup_screen.py

import configparser
import pathlib

from textual import on
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

    def on_mount(self) -> None:
        self.title = "SMTP Setup"
        if not self.smtp_config.exists():
            self.create_config()

        config = configparser.ConfigParser()
        config.read(self.smtp_config)

        self.smtp_server.value = config.get("SMTP Settings", "server")
        self.port.value = config.get("SMTP Settings", "port")
        self.username.value = config.get("SMTP Settings", "username")

    def action_exit_screen(self) -> None:
        self.dismiss()

    @on(Button.Pressed, "#save_smtp")
    def on_save(self) -> None:
        """
        Save the SMTP configuration
        """
        if not self.smtp_server.value:
            self.app.notify("SMTP Server is required!", title="Error", severity="error")
            return
        if not self.port.value:
            self.app.notify("SMTP Port is required!", title="Error", severity="error")
            return
        if not self.username.value:
            self.app.notify("SMTP Username is required!", title="Error", severity="error")
            return

        self.update_config()
        self.dismiss()

    @on(Button.Pressed, "#cancel_smtp")
    def on_cancel(self) -> None:
        """
        Cancel the Setup SMTP screen
        """
        self.dismiss()

    def create_config(self) -> None:
        """
        Create the SMTP configuration file
        """
        config = configparser.ConfigParser()
        config.add_section("SMTP Settings")
        config.set("SMTP Settings", "server", "SERVER")
        config.set("SMTP Settings", "port", "25")
        config.set("SMTP Settings", "username", "USERNAME")

        with open(self.smtp_config, "w") as config_file:
            config.write(config_file)

    def update_config(self) -> None:
        """
        Update the SMTP configuration file
        """
        config = configparser.ConfigParser()
        config.read(self.smtp_config)

        config.set("SMTP Settings", "server", self.smtp_server.value)
        config.set("SMTP Settings", "port", self.port.value)
        config.set("SMTP Settings", "username", self.username.value)

        with open(self.smtp_config, "w") as config_file:
            config.write(config_file)