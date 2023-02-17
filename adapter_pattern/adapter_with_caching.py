class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end="")  # thus, we need to represent Line from our API as a series of Points (above) to make it work

# ^^^ we are given this API ^^^


# our existing API
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter:  # adapter
    cache = {}

    def __init__(self, line):
        super().__init__()
        self.h = hash(line)
        if self.h in self.cache:
            return

        print(f"Generating points for line "
              f"[{line.start.x}, {line.start.y}]->"
              f"[{line.end.x}, {line.end.y}]")

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = max(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])


def draw(recs):
    print("\n\n--- Drawing some staff ---\n")
    for rectangle in recs:
        for line in rectangle:
            adapter = LineToPointAdapter(line)
            for p in adapter:  # completing adapter
                draw_point(p)  # using initial API to which we adapted our system


if __name__ == "__main__":
    rectangles = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rectangles)
    draw(rectangles)
