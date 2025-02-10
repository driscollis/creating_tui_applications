# weather_app.py

from textual.app import App, ComposeResult
from textual.containers import Horizontal, HorizontalGroup, VerticalScroll, Vertical
from textual.widgets import Button, Label, Header, Input


class Weather(HorizontalGroup):

    def __init__(self, postal_code: str) -> None:
        super().__init__()
        self.postal_code = postal_code

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Location", id=f"location_{self.postal_code}"),
            Label("Current Temp", id=f"current_temp_{self.postal_code}"),
            Label("", id=f"wmo_{self.postal_code}"),
        )
        yield Vertical(
            Label("Weekday +1", id=f"plus_one_{self.postal_code}"),
            Label("Temp", id=f"plus_one_temp_{self.postal_code}"),
            Label("Weather", id=f"plus_one_weather_{self.postal_code}")
        )
        yield Vertical(
            Label("Weekday +2", id=f"plus_two_{self.postal_code}"),
            Label("Temp", id=f"plus_two_temp_{self.postal_code}"),
            Label("Weather", id=f"plus_two_weather_{self.postal_code}")
        )
        yield Vertical(
            Label("Weekday +3", id=f"plus_three_{self.postal_code}"),
            Label("Temp", id=f"plus_three_temp_{self.postal_code}"),
            Label("Weather", id=f"plus_three_weather_{self.postal_code}")
        )


class WeatherApp(App):

    #CSS_PATH = "weather.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Input(placeholder="Postal Code", id="postal_code"),
            Button("Add Weather", id="add_weather"),
            id="add_weather"
        )
        yield VerticalScroll(Weather("50310"), Weather("75001"), id="vertical_scroll")


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
