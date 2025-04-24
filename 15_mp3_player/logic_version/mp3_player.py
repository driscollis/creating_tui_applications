# mp3_player.py

import pathlib

import eyed3
import vlc

import data_processor
from screens import FileBrowser

from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Center
from textual.widgets import Button, DataTable, DirectoryTree
from textual.widgets import Header, Footer


class MP3Player(App):
    CSS_PATH = "mp3_player.tcss"
    BINDINGS = [
        ("ctrl+l", "load", "Load Music"),
        ("escape", "esc", "Exit dialog"),
        ("p", "previous", "Previous"),
        ("n", "next", "Next")
    ]

    def __init__(self) -> None:
        super().__init__()
        self.current_track = ""
        self.id3 = None
        self.player = None
        self.mp3_data = [("No Music Found", "", ""),
                         ("Press CTRL+L to load music files", "", "")]
        self.app_selected_file = pathlib.Path("")
        self.current_track_index = 1

    def load_mp3(self) -> None:
        """
        Load the MP3 file into the music player and EyeD3
        """
        self.id3 = eyed3.load(self.current_track)
        self.player = vlc.MediaPlayer(self.current_track)

    def compose(self) -> ComposeResult:
        play = Text.from_markup(":play_button:")
        pause = Text.from_markup(":pause_button:")
        stop = Text.from_markup(":stop_button:")
        prev = Text.from_markup(":last_track_button:")
        nxt =  Text.from_markup(":next_track_button:")

        self.prev_btn = Button(prev, id="prev")
        self.play_btn = Button(play, id="play")
        self.next_btn = Button(nxt, id="nxt")
        self.stop_btn = Button(stop, id="stop")
        self.pause_btn = Button(pause, id="pause")
        self.title = "No Music Playing"
        yield Header()
        yield Vertical(
            DataTable(id="playlist"),
            Center(
                Horizontal(
                    self.stop_btn,
                    self.prev_btn,
                    self.play_btn,
                    self.next_btn,
                    self.pause_btn,
                    id="player-buttons"
                ),
            ),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if self.current_track is None:
            return
        elif self.current_track and self.player is None:
            self.load_mp3()

        if event.button.id == "play" and self.current_track:
            event.button.styles.background = "green"
            self.pause_btn.styles.background = None
            self.stop_btn.styles.background = None

            self.play_track()
        elif event.button.id == "pause":
            event.button.styles.background = "green"
            self.play_btn.styles.background = None
            self.stop_btn.styles.background = None

            if self.player:
                self.player.pause()
            self.title = f"Paused: {self.id3.tag.title} by {self.id3.tag.artist}"
        elif event.button.id == "stop":
            event.button.styles.background = "red"
            self.play_btn.styles.background = None
            self.pause_btn.styles.background = None

            if self.player is not None:
                self.player.stop()

            self.title = "Music Stopped!"

    @on(Button.Pressed, "#nxt")
    def on_next_track(self) -> None:
        self.action_next()

    @on(Button.Pressed, "#prev")
    def on_prev_track(self) -> None:
        self.action_previous()

    def on_file_browser_selected(self, message: FileBrowser.Selected) -> None:
        """
        Message handler - Called when a custom message is posted from FileBrowser
        """
        self.app.pop_screen()

        # Parse the file
        self.mp3_data = data_processor.process_mp3s(self.app_selected_file)

        # Load the DataTable
        table: DataTable = self.query_one(DataTable)
        table.clear(columns=True)
        table.add_columns(*self.mp3_data[0])
        table.add_rows(self.mp3_data[1:])
        table.cursor_type = "row"
        table.border_title = "Playlist"

        self.current_track =  self.mp3_data[1][-1]

    @on(DirectoryTree.FileSelected)
    @on(DirectoryTree.DirectorySelected)
    def on_file_selection(
        self,
        event: DirectoryTree.FileSelected | DirectoryTree.DirectorySelected
        ) -> None:
        """
        Called when the FileSelected message is emitted from the DirectoryTree
        """
        self.app_selected_file = event.path

    def on_mount(self) -> None:
        table: DataTable = self.query_one(DataTable)
        table.clear(columns=True)
        table.add_columns(*self.mp3_data[0])
        table.add_rows(self.mp3_data[1:])
        table.cursor_type = "row"
        table.border_title = "Playlist"

    @on(DataTable.RowSelected)
    def on_music_selected(self, event: DataTable.RowSelected) -> None:
        self.current_track = self.mp3_data[event.cursor_row + 1][-1]

        if event.cursor_row + 1 <= len(self.mp3_data):
            self.current_track_index = event.cursor_row

    def action_esc(self) -> None:
        """
        Exit a screen but not the application itself

        Works with any screen except the main one
        """
        try:
            self.app.pop_screen()
        except:
            pass

    def action_load(self) -> None:
        """
        Action called with ctrl+L - shows file browser
        """
        self.push_screen(FileBrowser())

    def action_next(self) -> None:
        """
        Action called when user presses "n" - Goes to next track, if it exists
        """
        if self.current_track_index < len(self.mp3_data) - 1:
            self.current_track_index += 1
            self.current_track = self.mp3_data[self.current_track_index][-1]
            self.play_track()
            self.notify(f"Now Playing: {self.current_track}", title="Track Change Forward")

    def action_previous(self) -> None:
        """
        Action called when user presses "p" - Goes the previous track, if possible
        """
        if self.current_track_index > 1:
            self.current_track_index -= 1
            self.current_track = self.mp3_data[self.current_track_index][-1]
            self.play_track()
            self.notify(f"Now Playing: {self.current_track}", title="Track Change Backward")

    def play_track(self):
        """
        Play the currently selected track
        """
        if self.player.is_playing():
            self.player.stop()
        self.load_mp3()
        self.player.play()
        self.title = f"Playing: {self.id3.tag.title} by {self.id3.tag.artist}"

if __name__ == "__main__":
    app = MP3Player()
    app.run()
