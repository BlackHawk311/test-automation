def to_uppercase(value: str) -> str:
    if not value:
        return value

    if not isinstance(value, str):
        return "This value is not a string."

    return value.upper()


def to_lowercase(value: str) -> str:
    if not value:
        return value

    if not isinstance(value, str):
        return "This value is not a string."

    return value.lower()


def capitalize(value: str) -> str:
    if not value:
        return value

    if not isinstance(value, str):
        return "This value is not a string."

    return value.capitalize()


def truncate(value: str, n_char: int) -> str:
    if not value:
        return value

    if len(value) < n_char:
        return value

    if not isinstance(value, str):
        return "This value is not a string."

    return value[:n_char] + '...'
