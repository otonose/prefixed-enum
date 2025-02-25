from prefixed_enum import PrefixedStrEnum, PrefixedDictEnum


class Monka(PrefixedStrEnum):
    __PREFIX__ = "https://domain.com"

    LOGIN = "/login"


class Omega(PrefixedDictEnum):
    __PREFIX__ = {"Host": "domain.com"}

    LOGIN = {
        "x-requested-with": "XMLHttpRequest",
    }


print(Monka.LOGIN)
print(Monka.LOGIN.value)
print(Omega.LOGIN)
print(Omega.LOGIN.value)
