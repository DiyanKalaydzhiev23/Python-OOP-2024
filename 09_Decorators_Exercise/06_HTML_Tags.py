def tags(tag: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        return wrapper

    return decorator


@tags('body')
@tags('div')
@tags('p')
def say_hi():
    return "Hello"


print(say_hi())
