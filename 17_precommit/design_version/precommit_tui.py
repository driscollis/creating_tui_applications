# precommit_tui.py

import pathlib
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Input
from textual.widgets import RichLog


class PrecommitApp(App):

    CSS_PATH = "precommit.tcss"

    def __init__(self) -> None:
        super().__init__()
        current_dir = pathlib.Path.cwd()
        self.config = current_dir / ".pre-commit-config.yaml"
        if not self.config.exists():
            self.config = pathlib.Path("No config found")

    def compose(self) -> ComposeResult:
        config_path = Input(value=str(self.config), id="config_path")
        config_path.border_title = "pre-commit config path"

        yield Vertical(
            config_path,
            Horizontal(
                Button("Edit Config", id="edit_config"),
                Button("Create Sample Config", id="sample_config"),
                Button("Install Git Hooks", id="install_hooks"),
                Button("Run pre-commit", id="run_precommit")
                ),
            RichLog(id="log"),
            id="vertical"
        )


if __name__ == "__main__":
    app = PrecommitApp()
    app.run()
