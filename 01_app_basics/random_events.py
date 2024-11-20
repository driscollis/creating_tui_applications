# random_events.py

import random

from textual.app import App
from textual import events

COLORS = [
    "red",
    "blue",
    "purple",   
    "teal",
    "white"
]


class RandomEventsApp(App):

    def on_mount(self) -> None:
        self.screen.styles.background = "darkgreen"
        
    def on_key(self) -> None:
        self.screen.styles.background = random.choice(COLORS)
        
        
if __name__ == "__main__":
    app = RandomEventsApp()
    app.run()
