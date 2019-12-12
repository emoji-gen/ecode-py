# -*- encoding: utf-8 -*-

import enum
from collections.abc import Set
from enum import IntEnum
from typing import AbstractSet


@enum.unique
class EcodeLocale(IntEnum):
    JA = 0
    KO = 1
    ZH_HANT = 2
    ZH_HANS = 3
    EN = 4

    @classmethod
    def from_name(cls, name: str):
        return cls[name.upper().replace('-', '_')]


@enum.unique
class EcodeFlag(IntEnum):
    SIZE_FIXED = 0
    STRETCH = 1


class EcodeV1:
    def __init__(self, *,
                 text: str,
                 locale: EcodeLocale = EcodeLocale.JA,
                 flags: AbstractSet[EcodeFlag] = frozenset()):
        if not text:
            raise ValueError('empty string is not allowed')

        if not isinstance(locale, EcodeLocale):
            raise ValueError('`locale` must be an instance of `EcodeLocale`, but it is ' + repr(locale))

        if not isinstance(flags, Set):
            raise ValueError('`flags` must be an instance of `Set`, but it is ' + repr(flags))

        self.text = text
        self.locale = locale
        self.flags = flags
