# class SomeObject:
#     def __init__(self):
#         self.integer_field = 0
#         self.float_field = 0.0
#         self.string_field = ""

class EventGet:
    def __init__(self, kind):
        self.value = None
        self.kind = {int: "EVENT_INT", float: "EVENT_FLOAT", str: "EVENT_STR"}[kind]


class EventSet:
    def __init__(self, value):
        self.kind = {int: "EVENT_INT", float: "EVENT_FLOAT", str: "EVENT_STR"}[type(value)]
        self.value = value


class NullHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, obj, event):
        if self.successor:
            self.successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == "EVENT_INT":
            if event.value is None:
                return obj.integer_field
            else:
                obj.integer_field = event.value
        else:
            super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == "EVENT_FLOAT":
            if event.value is None:
                return obj.float_field
            else:
                obj.float_field = event.value
        else:
            super().handle(obj, event)
        # if isinstance(event, EventGet):
        #     return object.float_field
        # elif isinstance(event, EventSet):
        #     object.float_field = event.value
        # else:
        #     super().handle(object, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == "EVENT_STR":
            if event.value is None:
                return obj.string_field
            else:
                obj.string_field = event.value
        else:
            super().handle(obj, event)
        # if isinstance(event, EventGet):
        #     return object.string_field
        # elif isinstance(event, EventSet):
        #     object.string_field = event.value
        # else:
        #     super().handle(object, event)


# obj1 = SomeObject()
# obj1.integer_field = 42
# obj1.float_field = 3.14
# obj1.string_field = "some text"
#
# chain = IntHandler(FloatHandler(StrHandler(NullHandler)))



