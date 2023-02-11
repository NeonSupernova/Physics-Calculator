class History:
    def __init__(self):
        self.history = []

    def __str__(self):
        return str(self.history)

    def __repr__(self):
        return self.__str__()

    def history_closure(self):
        def foo(func):
            def wrapper(*args):
                return func(*args, history=self)

            return wrapper

        return foo
