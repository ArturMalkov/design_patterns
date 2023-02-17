"""
Reflective visitor - includes type checking
"""


from abc import ABC


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:  # outsourced printing functionality to this external class (separation of concerns)
    @staticmethod
    def print(expression, buffer):
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(")")

    Expression.print = lambda self, buffer: ExpressionPrinter.print(self, buffer)


if __name__ == "__main__":
    # 1 + (2+3) - need to print it
    expression = AdditionExpression(
        DoubleExpression(1),  # left side
        AdditionExpression(  # right side
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    expression.print(buffer)
    ExpressionPrinter.print(expression, buffer)
    print("".join(buffer))
