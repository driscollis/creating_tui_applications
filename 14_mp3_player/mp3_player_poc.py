# mp3_player_poc.py

import vlc

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button


class MP3Player(App):

    def __init__(self) -> None:
        super().__init__()
        self.player = None
        self.current_track = r"PATH TO MP3 FILE"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("Play", id="play", variant="primary"),
            Button("Stop", id="stop", variant="error")
        )

    @on(Button.Pressed, "#play")
    def on_play(self) -> None:
        self.player = vlc.MediaPlayer(self.current_track)
        self.player.play()

    @on(Button.Pressed, "#stop")
    def on_stop(self) -> None:
        self.player.stop()


if __name__ == "__main__":
    app = MP3Player()
    app.run()
