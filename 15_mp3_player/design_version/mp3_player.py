# mp3_player.py

from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Center
from textual.widgets import Button, DataTable
from textual.widgets import Header, Footer


class MP3Player(App):
    CSS_PATH = "mp3_player.tcss"

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

if __name__ == "__main__":
    app = MP3Player()
    app.run()
