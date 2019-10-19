# -*- encoding: utf-8 -*-

import enum
from enum import IntEnum


@enum.unique
class EcodeLocale(IntEnum):
    JA = 0
    KO = 1
    ZH_HANT = 2
    ZH_HANS = 3
    EN = 4

    @classmethod
    def from_name(cls, name):
        return cls[name.upper().replace('-', '_')]


@enum.unique
class EcodeFlag(IntEnum):
    SIZE_FIXED = 0
    STRETCH = 1


class EcodeV1():
    def __init__(self, *,
            text=None,
            locale=EcodeLocale.JA,
            flags=set()):
        if not text:
            raise ValueError('empty string is not allowed')

        if not isinstance(locale, EcodeLocale):
            raise ValueError('Illegal locale : ' + repr(locale))

        if not isinstance(flags, set):
            raise ValueError('Illegal flags : ' + repr(flags))

        self.text = text
        self.locale = locale
        self.flags = flags
