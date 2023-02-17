"""
Facade pattern provides unified interface to a set of interfaces in a subsystem.  Facade defines a high-level interface
that makes the subsystem easier to use.

Underneath the facade we have lots of classes, etc., but on the outside we don't have to deal with all that all the time.
To do this, we create a nice wrapper, interface that we (client) can interact with instead.
Facade interacts with all the inner workings of a program and simplifies that interaction for you.
Law of Demeter (the principle of least knowledge) - "talk to your immediate friends" - objects should talk to their
immediate friends (not the friends of their friends) (aimed at reducing coupling).

Facade pattern provides a simple, easy-to-use/understand user interface (API) over a large and sophisticated body of code.

Motivation:
- balancing complexity and presentation/usability
- there are many systems working internally with complex structure but API consumers want it to "just work"
"""

# console facade


class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [" "] * (width*height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index+self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:  # facade
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):  # high-level API
        self.current_viewport.append(text)

    def get_char_at(self, index):  # low-level API
        return self.current_viewport.get_char_at(index)


if __name__ == "__main__":
    console = Console()
    console.write("Hello")
