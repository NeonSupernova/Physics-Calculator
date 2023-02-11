from functions.History import History
CONSTANTS = {
    "gravity": 9.80,
    "speed_of_light": 299792458,
    "absolute_zero": -273.15
}
hist = History()


@hist.history_closure()
def query_hist(inp: str, **kwargs):
    if inp.startswith('$'):
        var = int(inp.split('$')[1]) + 1
        if 0 < var <= len(kwargs['history'].history):
            x = kwargs['history'].history[var - 1]
            return True, x
        else:
            return False, 'Index Out of Range: [%i...%i]' % (0, len(kwargs["history"].history))
    else:
        return True, inp


def multi_numeric_input(*args: str) -> tuple[float, ...]:
    while True:
        try:
            x = ()
            for i in args:
                query, case = query_hist(input(f"Enter value for {i}: "))
                if query:
                    x += (float(case),)
                else:
                    raise ValueError(case)
            return x
        except ValueError as e:
            print('Bad Value, try again')
            print(e)
