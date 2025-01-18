from enum import StrEnum


class PrefixedEnum(StrEnum):
    """
    Use `__PREFIX__` for prefix.
    """

    __PREFIX__ = ""

    def __new__(cls, value: str):
        prefix = "__PREFIX__"
        if hasattr(cls, prefix):
            root: PrefixedEnum = getattr(cls, prefix)
            value = root + value
        obj = str.__new__(cls, value)
        return obj
