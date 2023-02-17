# classic Visitor pattern - double dispatch visitor (see two "visit" methods below)

# Visitor decorator code below


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


# ↑↑↑ LIBRARY CODE ↑↑↑


class DoubleExpression:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, double_exp):
        self.buffer.append(str(double_exp.value))

    @visitor(AdditionExpression)
    def visit(self, addition_exp):
        self.buffer.append("(")
        # addition_exp.left.accept(self)
        self.visit(addition_exp.left)
        self.buffer.append("+")
        # addition_exp.right.accept(self)
        self.visit(addition_exp.right)
        self.buffer.append(")")

    def __str__(self):
        return "".join(self.buffer)


class ExpressionEvaluator:
    def __init__(self):
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, double_exp):
        self.value = double_exp.value

    @visitor(AdditionExpression)
    def visit(self, addition_exp):
        self.visit(addition_exp.left)
        temp = self.value
        self.visit(addition_exp.right)
        self.value += temp


if __name__ == "__main__":
    # 1 + (2+3) - need to print it
    expr = AdditionExpression(
        DoubleExpression(1),  # left side
        AdditionExpression(  # right side
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    printer = ExpressionPrinter()
    printer.visit(expr)

    evaluator = ExpressionEvaluator()
    evaluator.visit(expr)

    print(f"{printer} = {evaluator.value}")
