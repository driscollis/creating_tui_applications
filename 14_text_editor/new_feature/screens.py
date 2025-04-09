# screens.py

from textual import on
from textual.app import ComposeResult
from textual.containers import Grid
from textual.message import Message
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, DirectoryTree, Footer, Header, Input, Label, OptionList, TextArea


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
            Button("Yes", variant="default", id="yes"),
            Button("No", id="no"),
            id="warning_dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when the OK button - dismisses the screen
        """
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)
        event.stop()


class SaveFileDialog(Screen):
    class Selected(Message):
        """
        File selected message
        """

        def __init__(self, filename: str) -> None:
            self.filename = filename
            super().__init__()

    def __init__(self) -> None:
        super().__init__()
        self.title = "Save File"
        self.root = "c:/"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Grid(
            Label(f"Folder name: {self.root}", id="folder"),
            DirectoryTree(self.root, id="directory"),
            Input(placeholder="filename.txt", id="filename"),
            Button("Save File", variant="primary", id="save_file"),
            id="save_dialog"
        )
        yield Footer()

    def on_mount(self) -> None:
        """
        Focus the input widget so the user can name the file
        """
        self.query_one("#filename").focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when the load file button is pressed
        """
        event.stop()
        filename = self.query_one("#filename").value
        self.post_message(self.Selected(filename))

    @on(DirectoryTree.DirectorySelected)
    def on_directory_selection(self, event: DirectoryTree.DirectorySelected) -> None:
        """
        Called when the DirectorySelected message is emitted from the DirectoryTree
        """
        self.query_one("#folder").update(f"Folder name: {event.path}")


class ThemeScreen(Screen):

    def __init__(self) -> None:
        super().__init__()
        self.current_selection = None

    def compose(self) -> ComposeResult:
        text_area = TextArea()
        self.title = "Change Theme"
        themes = list(text_area.available_themes)
        themes.sort()
        yield Grid(
            Header(),
            OptionList(*themes, id="themes"),
            Button("Apply Theme", id="theme_btn"),
            id="theme_dialog"
        )

    def on_mount(self) -> None:
        self.query(OptionList).focus()

    @on(OptionList.OptionHighlighted)
    @on(OptionList.OptionSelected)
    def on_item(self, event) -> None:
        self.current_selection = event.option.prompt

    @on(Button.Pressed)
    def on_apply_theme(self) -> None:
        self.dismiss(self.current_selection)
