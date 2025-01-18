from prefixed_enum import PrefixedEnum


class Monka(PrefixedEnum):
    __PREFIX__ = "https://domain.com"

    LOGIN = "/login"


print(Monka.LOGIN)
