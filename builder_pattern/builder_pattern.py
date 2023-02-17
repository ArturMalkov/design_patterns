"""
Builder pattern's essence - when piecewise object construction is complicated, provide an API for doing it succinctly.

Motivation:
- Some objects require a lot of ceremony to create (not in a single initializer call - but in stages)
- Having an object with 10 initializer arguments is not productive.
- Instead, opt for piecewise construction.

Builder provides an API for constructing an object step-by-step.
Different facets (aspects) of an object can be built with different builders (sub-builders) working in tandem via a base class
Builders often have fluent interface (return "self") which makes it possible to chain several builders together.
"""

text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))

words = ["hello", "world"]
parts = ["<ul>"]
for w in words:
    parts.append(f"   <li>{w}</li>")
parts.append("</ul>")
print("\n".join(parts))

# Instead #


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):  # alternative to starting using the builder
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self  # to chain invocations one after another (see below)

    def __str__(self):
        return str(self.__root)


print("-----")
# builder = HtmlBuilder("ul")
builder = HtmlElement.create("ul")
builder.add_child("li", "hello")
builder.add_child("li", "world")
print("Ordinary builder:")
print(builder)

builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")  # chaining invocations one after another
