# precommit_tui.py

import pathlib
import subprocess
import textwrap

from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Input
from textual.widgets import RichLog

from screens import EditScreen, WarningScreen


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

    @on(Button.Pressed, "#edit_config")
    def on_edit_config(self) -> None:
        if self.config.exists():
            self.push_screen(EditScreen(self.config))

    @on(Button.Pressed, "#sample_config")
    def on_create_sample_config(self) -> None:
        """
        Event handler - Creates a sample pre-commit config
        """

        def overwrite(affirmative: bool):
            """
            Callback method for Warning Screen about overwriting a file
            """
            if affirmative:
                self.create_sample_config()

        if self.config.exists():
            # warn user
            warning_message = "Config file already exists! Do you want to overwrite it?"
            self.push_screen(WarningScreen(warning_message), overwrite)
        else:
            self.create_sample_config()

    @on(Button.Pressed, "#install_hooks")
    def on_install_hooks(self) -> None:
        """
        Event handler - installs git hooks
        """
        self.install_hooks()

    @on(Button.Pressed, "#run_precommit")
    def on_run_pre_commit(self) -> None:
        """
        Run pre-commit on all files in local repo
        """
        if self.config.exists():
            self.run_pre_commit()

    @work(exclusive=True, thread=True)
    def create_sample_config(self) -> None:
        """
        Create a simple sample config in the current working directory
        """
        sample_config = """
        # See https://pre-commit.com for more information
        # See https://pre-commit.com/hooks.html for more hooks
        repos:
        -   repo: https://github.com/pre-commit/pre-commit-hooks
            rev: v3.2.0
            hooks:
            -   id: trailing-whitespace
            -   id: end-of-file-fixer
            -   id: check-yaml
            -   id: check-added-large-files
        """
        sample_config_path = pathlib.Path.cwd() / ".pre-commit-config.yaml"
        with open(sample_config_path, "w") as config:
            config.write(textwrap.dedent(sample_config))
        self.notify(f"Sample config written to {sample_config_path}")
        self.query_one("#config_path").value = str(sample_config_path)
        self.config = sample_config_path

    @work(exclusive=True, thread=True)
    def install_hooks(self) -> None:
        """
        Install the pre-commit Git hooks
        """
        cmd = ["pre-commit", "install"]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            text_log = self.query_one(RichLog, RichLog)
            text_log.write(result.stdout)
            self.notify("Git Hooks installed successfully!", title="Success")
        except FileNotFoundError:
            self.notify("pre-commit not found! Make sure pre-commit is installed!",
                        title="Error", severity="error")

    @work(exclusive=True, thread=True)
    def run_pre_commit(self) -> None:
        cmd = ["pre-commit", "run", "--all-files"]
        text_log = self.query_one(RichLog, RichLog)
        try:
            text_log.write("Running pre-commit on all files")
            result = subprocess.run(cmd, capture_output=True, text=True)
            text_log.write(result.stdout)
            self.notify("Git Hooks installed successfully!", title="Success")
        except FileNotFoundError:
            self.notify("pre-commit not found! Make sure pre-commit is installed!",
                        title="Error", severity="error")


if __name__ == "__main__":
    app = PrecommitApp()
    app.run()
