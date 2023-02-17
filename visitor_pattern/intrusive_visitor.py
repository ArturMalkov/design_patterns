"""
Intrusive visitor modifies existing classes, thus violating open-closed principle.
"Buffer" below is an object that is visiting both DoubleExpression and AdditionExpression
"""


class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer):  # intrusion - method added
        buffer.append(str(self.value))

    def eval(self):
        return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer):  # intrusion - method added
        buffer.append("(")
        self.left.print(buffer)
        buffer.append("+")
        self.right.print(buffer)
        buffer.append(")")

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == "__main__":
    # 1 + (2+3) - need to print it
    e = AdditionExpression(
        DoubleExpression(1),  # left side
        AdditionExpression(  # right side
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    e.print(buffer)
    print("".join(buffer), " = ", e.eval())
