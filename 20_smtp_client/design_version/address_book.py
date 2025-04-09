# address_book.py

import pathlib

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, DataTable, Footer, Header, Input


class AddressForm(ModalScreen):

    CSS_PATH = "address_form.tcss"

    def __init__(self, title: str = "Add New Record",
                 initial_data: list | None = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title

        self.initial_data = initial_data if initial_data else ["", "", "", ""]

    def compose(self) -> ComposeResult:
        first, last, email, phone = self.initial_data
        self.first_name = Input(first, id="first_name")
        self.first_name.border_title = "First Name"

        self.last_name = Input(last, id="last_name")
        self.last_name.border_title = "Last Name"

        self.email = Input(email, id="email_address")
        self.email.border_title = "Email"

        yield Header()
        yield Vertical(
            self.first_name,
            self.last_name,
            self.email,
            Horizontal(
                Button("Save", id="save_address", variant="primary"),
                Button("Cancel", id="cancel_address", variant="error"),
                id="address_form_buttons"
            )
        )


class AddressBook(ModalScreen):

    CSS_PATH = "address_book.tcss"
    BINDINGS = [("escape", "exit_screen", "Exit")]

    def __init__(self, get_address: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.address_book_path = pathlib.Path("addresses.csv")
        self.title = "Address Book"
        self.selected_row = None
        self.selected_row_key = None
        self.get_address = get_address

    def compose(self) -> ComposeResult:
        yield Header()
        if not self.get_address:
            yield Vertical(
                DataTable(id="address_book"),
                Horizontal(
                    Button("New Address", id="new_address", variant="primary"),
                    Button("Edit Address", id="edit_address", variant="error"),
                    id="horizontal_buttons"
                ),
                id="address_book_dlg"
            )
        else:
            yield Vertical(
                DataTable(id="address_book"),
                Horizontal(
                    Button("OK", id="get_address", variant="primary"),
                    Button("Cancel", id="cancel_address", variant="error"),
                    id="horizontal_buttons"
                ),
                id="address_book_dlg"
            )

        yield Footer()

