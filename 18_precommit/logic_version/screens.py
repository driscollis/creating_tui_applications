# screens.py

import pathlib
import yaml

from textual import on
from textual.app import ComposeResult
from textual.containers import Grid, Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Header, Label, TextArea

class EditScreen(ModalScreen):

    def __init__(self, path: str,
                 name: str | None = None,
                 id: str | None = None,
                 classes: str | None = None) -> None:
        super().__init__(name, id, classes)
        self.path = path
        self.title = f"Editing: {self.path}"

        with open(self.path) as config:
            self.data = config.read()

    def compose(self) -> ComposeResult:
        yield Vertical(
            Header(),
            TextArea(self.data, language="yaml", id="config_data"),
            Horizontal(
                Button.success("Save", id="save_config"),
                Button.warning("Cancel", id="cancel"),
                ),
            id="edit_screen"
        )

    @on(Button.Pressed, "#cancel")
    def on_cancel(self) -> None:
        """
        Event handler - Cancel editing config
        """
        self.dismiss()

    @on(Button.Pressed, "#save_config")
    def on_save_config(self) -> None:
        """
        Event handler - Save config
        """
        text = self.query_one("#config_data", TextArea).text
        parsed_yaml = yaml.safe_load(text)
        test_path = pathlib.Path.cwd() / "pre-commit-config.yaml"
        with open(test_path, "w") as config:
            yaml.dump(parsed_yaml, config)
        self.notify("Saved pre-commit config changes!")
        self.dismiss()


class WarningScreen(ModalScreen):
    """
    Creates a pop-up Screen that displays a warning message to the user
    """

    def __init__(self, warning_message: str,
                 name: str | None = None,
                 id: str | None = None,
                 classes: str | None = None) -> None:
        super().__init__(name, id, classes)
        self.warning_message = warning_message

    def compose(self) -> ComposeResult:
        """
        Create the UI in the Warning Screen
        """
        yield Grid(
            Label(self.warning_message, id="warning_msg"),
            Button.success("Yes", id="yes"),
            Button.warning("No", id="no"),
            id="warning_dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when a button is pressed - dismisses the screen
        """
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)
        event.stop()
