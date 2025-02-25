from __future__ import annotations

from enum import Enum
from typing import Any


class PrefixedEnum(Enum):
    pass

    # def __str__(self):
    #     return str(self.value)


class PrefixedStrEnum(str, PrefixedEnum):
    """
    Use `__PREFIX__` for prefix.
    """

    def __new__(cls, value: str):
        value = cls.__PREFIX__ + value
        obj = super().__new__(cls, value)
        obj._value_ = value
        return obj

    __PREFIX__ = ""


class PrefixedDictEnum(dict[Any, Any], PrefixedEnum):
    """
    Use `__PREFIX__` for prefix.
    """

    def __new__(cls, value: dict[Any, Any]):
        value = cls.__PREFIX__ | value
        obj = super().__new__(cls, value)
        obj._value_ = value
        return obj

    __PREFIX__: dict[Any, Any] = {}


class PrefixedListEnum(list[Any], PrefixedEnum):
    """
    Use `__PREFIX__` for prefix.
    """

    def __new__(cls, value: list[Any]):
        value = cls.__PREFIX__ + value
        obj = super().__new__(cls, value)
        obj._value_ = value
        return obj

    __PREFIX__: list[Any] = []


class PrefixedTupleEnum(tuple[Any, ...], PrefixedEnum):
    """
    Use `__PREFIX__` for prefix.
    """

    def __new__(cls, value: tuple[Any, ...]):
        value = cls.__PREFIX__ + value
        obj = super().__new__(cls, value)
        obj._value_ = value
        return obj

    __PREFIX__: tuple[Any, ...] = ()


class PrefixedSetEnum(set[Any], PrefixedEnum):
    """
    Use `__PREFIX__` for prefix.
    """

    def __new__(cls, value: set[Any]):
        value = cls.__PREFIX__ | value
        obj = super().__new__(cls, value)
        obj._value_ = value
        return obj

    __PREFIX__: set[Any] = set()


class PrefixedIntEnum(int, PrefixedEnum):
    """
    Use `__PREFIX__` for prefix.
    """

    def __new__(cls, value: int):
        value = cls.__PREFIX__ + value
        obj = super().__new__(cls, value)
        obj._value_ = value
        return obj

    __PREFIX__: int = 0
