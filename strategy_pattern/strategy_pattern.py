"""
Strategy pattern is mainly about using composition rather than inheritance (inheritance is not intended for code reuse).
Strategy pattern defines a family of algorithms, encapsulates each one and makes them interchangeable. Strategy lets
the algorithm vary independently of the clients that use it (through has-a relationship (i.e. composition) as opposed
to is-a relationship (inheritance)).
Decomposes algorithms into common parts + specifics via composition.
Dependency injection.

Enables the exact behavior of a system to be selected at runtime.
At runtime you specify the actual details (low-level), and then feed them in whatever component (high-level) is able to consume them
High-level algorithm expects strategies to conform to a particular interface.

- define an algorithm at a high-level
- define the interface you expect each strategy to follow
- provide for dynamic composition of strategies in the resulting object.
"""

from abc import ABC
from enum import Enum, auto


class ListStrategy(ABC):  # blueprint for an algorithm
    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        pass


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f" * {item}\n")


class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append("<ul>\n")

    def end(self, buffer):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f"  <li>{item}</li>\n")


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class TextProcessor:
    def __init__(self, list_strategy=HtmlListStrategy()):
        self.buffer = []
        self.list_strategy = list_strategy

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format_):
        if format_ == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format_ == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)


if __name__ == "__main__":
    items = ["foo", "bar", "baz"]

    text_processor = TextProcessor()
    text_processor.set_output_format(OutputFormat.MARKDOWN)
    text_processor.append_list(items)
    print(text_processor)

    text_processor.set_output_format(OutputFormat.HTML)
    text_processor.clear()
    text_processor.append_list(items)
    print(text_processor)
