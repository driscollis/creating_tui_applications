# rss_tui.py

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer, OptionList, Markdown


class FeedList(OptionList):
    pass


class ArticleList(OptionList):
    pass


class ArticleView(Markdown):
    pass


class RSSViewerApp(App):

    CSS_PATH = "rss_tui.tcss"

    def compose(self) -> ComposeResult:
        self.feeds = FeedList(*["No Feeds"], id="feeds")
        self.feeds.border_title = "Feed List"
        self.articles = ArticleList(*["None"], id="articles")
        self.articles.border_title = "Articles"
        markdown = ArticleView(id="article")
        markdown.border_title = "Markdown"

        yield Header()
        yield Grid(
            self.feeds,
            self.articles,
            markdown,
            id="rss_grid"
        )
        yield Footer()


if __name__ == "__main__":
    app = RSSViewerApp()
    app.run()
