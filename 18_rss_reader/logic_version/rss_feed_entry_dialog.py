# rss_feed_entry_dialog.py

from textual import on
from textual.app import ComposeResult
from textual.containers import Center, Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Header, Input, Label


class RSSFeedEntryDialog(ModalScreen):
    """
    Display a dialog that allows the user to enter some text and return it
    """

    def compose(self) -> ComposeResult:
        """
        Create the widgets for the TextEntryDialog's user interface
        """
        yield Vertical(
            Header(),
            Center(Label( "Enter RSS Feed URL", id="text_entry_label")),
            Input(placeholder="", id="answer"),
            Center(
                Horizontal(
                    Button("OK", variant="primary", id="text_entry_ok"),
                    Button("Cancel", variant="error", id="text_entry_cancel"),
                )
            ),
            id="text_entry_dlg",
        )

    def on_mount(self) -> None:
        """
        Set the focus on the input widget by default when the dialog is loaded
        """
        self.query_one("#answer").focus()

    @on(Button.Pressed, "#text_entry_ok")
    def on_ok(self, event: Button.Pressed) -> None:
        """
        Return the user's entry back to the calling application and dismiss the dialog
        """
        answer = self.query_one("#answer").value
        self.dismiss(answer)

    @on(Button.Pressed, "#text_entry_cancel")
    def on_cancel(self, event: Button.Pressed) -> None:
        """
        Returns an empty string to the calling application and dismisses the dialog
        """
        self.dismiss("")
