import functools

from console.utils import wait_key, cls
from functions.FluentBuffer import FluentBuffer
from functions.utils import hist


class Menu:
    def __init__(self, title, message, items=None, char_buf="="):
        if items is None:
            items = []
        self.menu_header = (
            FluentBuffer()
            .append(title)
            .append(char_buf * 20)
            .append(message)
            .append(char_buf * 20)
        )
        self.name = title
        self.items = items

    @property
    def history(self):
        return hist.history

    def add_option(self, func):
        @functools.wraps(func)
        def wrapper():
            print(f'{func.__name__} added')
        self.items.append(wrapper)
        return wrapper

    def display(self, level=0):
        print(self.menu_header)
        # print("\t" * level + self.name)
        for index, item in enumerate(self.items):
            if isinstance(item, Menu):
                print("\t" * (level + 1) + f"[{index + 1}] {item.name}")
            else:
                print("\t" * (level + 1) + f"[{index + 1}] {item.__name__}")
        print("\t" * (level + 1) + "[q] quit")

    @hist.history_closure()
    def run(self, **kwargs):
        while True:
            cls()
            print(hist.history)
            self.display()
            print("Enter your choice: ")
            choice = wait_key((lambda lst: tuple(str(i) for i in range(1, len(lst) + 1)) + ('q',))(self.items))
            if choice == "q":
                break
            choice = int(choice) - 1
            item = self.items[choice]
            if isinstance(item, Menu):
                item.run()
            else:
                value = item()
                print(value)
                if wait_key() == 's':
                    kwargs['history'].history.append(value)


