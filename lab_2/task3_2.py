def min_len_check(fn):
    def wrapper(arg: str):
        if len(arg) > 10:
            result = fn(arg)
            return result
        else:
            raise ValueError("Строка слишком короткая")

    return wrapper


@min_len_check
def some_func(str_arg: str):
    return str_arg


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
