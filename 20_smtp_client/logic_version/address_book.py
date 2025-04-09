# address_book.py

import csv
import pathlib

from textual import on
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

    @on(Button.Pressed, "#cancel_address")
    def on_cancel(self) -> None:
        self.dismiss({})

    @on(Button.Pressed, "#save_address")
    def on_save(self) -> None:
        self.dismiss([self.first_name.value,
                      self.last_name.value,
                      self.email.value])


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

    def on_mount(self) -> None:
        self.update_address_table()

    def process_csv(self) -> list[str]:
        """
        Process the CSV file and turn it into a list of lists
        """
        rows = []
        with open(self.address_book_path, newline="") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row:
                    rows.append(row)
        return rows

    def action_exit_screen(self) -> None:
        self.dismiss()

    @on(Button.Pressed, "#new_address")
    def on_new_address(self) -> None:
        self.app.push_screen(AddressForm(), self.add_new_record)

    @on(Button.Pressed, "#edit_address")
    def on_edit_address(self) -> None:
        if self.selected_row is not None:
            self.app.push_screen(
                AddressForm(
                    "Edit Address Record", self.selected_row), self.update_table_and_csv)

    @on(Button.Pressed, "#get_address")
    def on_get_address(self) -> None:
        """
        Return the currently selected email address
        """
        if self.selected_row:
            first, last, email, phone = self.selected_row
            self.dismiss(email)

    @on(Button.Pressed, "#cancel_address")
    def on_cancel_address(self) -> None:
        """
        Cancel the screen and return nothing
        """
        self.dismiss()

    @on(DataTable.RowSelected, "#address_book")
    @on(DataTable.RowHighlighted, "#address_book")
    def on_row_clicked(self, event: DataTable.RowSelected) -> None:
        table: DataTable = event.data_table
        self.selected_row = table.get_row(event.row_key)
        self.selected_row_key = event.row_key

    def add_new_record(self, new_data: list[str]) -> None:
        if not new_data:
            return

        if not self.address_book_path.exists():
            headers = ["First Name", "Last Name", "Email", "Phone"]
            with open(self.address_book_path, "w") as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(headers)
                writer.writerow(new_data)
        else:
            with open(self.address_book_path, "a") as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(new_data)

        self.update_address_table()

    def update_table_and_csv(self, new_data: list[str]) -> None:
        # Update the current selection and then loop over rows in table to write back out to CSV
        table = self.query_one(DataTable)
        for value, column in zip(new_data, table.columns):
            table.update_cell(self.selected_row_key, column, value, update_width=True)

        # Write data from table back to CSV
        headers = ["First Name", "Last Name", "Email", "Phone"]
        with open(self.address_book_path, "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(headers)
            for row in table.rows:
                row_values = table.get_row(row)
                writer.writerow(row_values)

    def update_address_table(self) -> None:
        if self.address_book_path.exists():
            rows = self.process_csv()
            table = self.query_one(DataTable)
            table.clear(columns=True)
            table.add_columns(*rows[0])
            table.add_rows(rows[1:])
            table.cursor_type = "row"
