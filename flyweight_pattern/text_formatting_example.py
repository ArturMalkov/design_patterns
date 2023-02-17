class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)  # inefficient

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for idx, val in enumerate(self.plain_text):
            result.append(val.upper() if self.caps[idx] else val)
        return "".join(result)


class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range

    def __str__(self):
        result = []
        for idx, val in enumerate(self.plain_text):
            for r in self.formatting:
                if r.covers(idx) and r.capitalize:
                    val = val.upper()
            result.append(val)
        return "".join(result)


if __name__ == "__main__":
    text = "This is a brave new world"
    ft = FormattedText(text)
    ft.capitalize(10, 15)
    print(ft)

    bft = BetterFormattedText(text)
    bft.get_range(16, 19).capitalize = True
    print(bft)
