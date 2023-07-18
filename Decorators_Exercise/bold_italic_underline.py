def make_bold(func):
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"

    return wrapper


def make_italic(func):
    def wrapper(*args):
        return f"<i>{func(*args)}</i>"

    return wrapper


def make_underline(func):
    def wrapper(*args):
        return f"<u>{func(*args)}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
