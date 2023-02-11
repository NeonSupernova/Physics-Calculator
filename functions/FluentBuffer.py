class FluentBuffer:
    def __init__(self):
        self.buf = ""

    def append(self, value):
        try:
            self.buf += (str(value) + "\n")
        except Exception as e:
            print(e)
        return self

    def __str__(self):
        return self.buf

    def __repr__(self):
        return self.__str__()
