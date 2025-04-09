# rss_tui.py

# https://www.blog.pythonlibrary.org/rss
# https://www.dailywire.com/feeds/rss.xml

import feedparser
from markdownify import markdownify as md

from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer, Markdown, OptionList
from textual.widgets.option_list import Option, Separator
from textual.worker import get_current_worker

from rss_feed_entry_dialog import RSSFeedEntryDialog


class FeedList(OptionList):
    pass


class ArticleList(OptionList):
    pass


class ArticleView(Markdown):
    pass


class RSSViewerApp(App):

    CSS_PATH = "rss_tui.tcss"
    BINDINGS = [
        ("ctrl+a", "add_feed", "Add Feed"),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.feed_titles = ["No Feeds Found"]
        self.feed_objects: dict[str, dict[str, dict]] = {}
        self.current_article = None
        self.current_feed_title = ""

    def compose(self) -> ComposeResult:
        self.feeds = FeedList(*self.feed_titles, id="feeds")
        self.feeds.border_title = "Feed List"
        self.articles = ArticleList(*["None"], id="articles")
        self.articles.border_title = "Articles"
        markdown = Markdown(id="article")
        markdown.border_title = "Markdown"

        yield Header()
        yield Grid(
            self.feeds,
            self.articles,
            markdown,
            id="rss_grid"
        )
        yield Footer()

    def action_add_feed(self) -> None:

        def add_feed_callback(feed_url: str) -> None:
            if feed_url:
                self.add_new_feed(feed_url)

        self.push_screen(RSSFeedEntryDialog(), add_feed_callback)

    @work(exclusive=True, thread=True, group="add_feed")
    def add_new_feed(self, feed_url: str) -> None:
        feed_obj = feedparser.parse(feed_url)
        self.feed_objects[feed_obj.feed.title] = {article.title: article for article in feed_obj.entries}
        self.current_feed_title = feed_obj.feed.title

        if self.feed_titles == ["No Feeds Found"]:
            self.call_from_thread(self.feeds.clear_options)
            self.feed_titles.clear()

        worker = get_current_worker()
        if feed_obj.feed.title not in self.feed_titles and not worker.is_cancelled:
            self.feed_titles.append(feed_obj.feed.title)
            self.call_from_thread(self._add_feed, feed_obj.feed.title)
            self.call_from_thread(self.articles.clear_options)
            self.call_from_thread(self._add_articles, self.feed_objects[feed_obj.feed.title])

            # TODO - Put in an exception handler
            self.current_article = self.feed_objects[self.current_feed_title][feed_obj.entries[0].title]
            self.call_from_thread(self.update_reader)


    def _add_feed(self, feed_title: str) -> None:
        """
        Add a new feed title and a separator
        """
        self.feeds.add_option(feed_title)
        self.feeds.add_option(Separator())

    def _add_articles(self, article_titles: list[str]) -> None:
        """
        For each article, also add a separator
        """
        for title in article_titles:
            self.articles.add_option(Option(title))
            self.articles.add_option(Separator())

    def update_reader(self) -> None:
        viewer = self.query_one("#article", Markdown)
        markdown = md(self.current_article.content[0]["value"])
        viewer.update(markdown)
        viewer.border_title = self.current_article.title

    @on(OptionList.OptionSelected, "#articles")
    def on_article_selected(self, event: OptionList.OptionSelected) -> None:
        self.current_article = self.feed_objects[self.current_feed_title][event.option.prompt]
        self.update_reader()

    @on(OptionList.OptionSelected, "#feeds")
    def on_feed_selected(self, event: OptionList.OptionSelected) -> None:
        self.current_feed_title = event.option.prompt
        self.articles.clear_options()
        self._add_articles(self.feed_objects[self.current_feed_title])
        for title in self.feed_objects[self.current_feed_title]:
            self.current_article = self.feed_objects[self.current_feed_title][title]
            break
        self.update_reader()


if __name__ == "__main__":
    app = RSSViewerApp()
    app.run()
