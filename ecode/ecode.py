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
    def from_code(cls, code: str):
        upper_code = code.upper()
        if upper_code == 'ZH':
            return cls.ZH_HANS

        return cls[upper_code.replace('-', '_')]


@enum.unique
class EcodeFlag(IntEnum):
    SIZE_FIXED = 0
    STRETCH = 1

    @classmethod
    def from_name(cls, code: str):
        return cls[code.upper()]


@enum.unique
class EcodeAlign(IntEnum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2

    @classmethod
    def from_name(cls, name: str):
        return cls[name.upper()]


@enum.unique
class EcodeSize(IntEnum):
    MDPI = (0, 128, 128)
    HDPI = (1, 192, 192)
    XHDPI = (2, 256, 256)
    XXHDPI = (3, 384, 384)

    # noinspection PyInitNewSignature
    def __new__(cls, value, width, height):
        obj = int.__new__(cls)
        obj._value_ = value
        obj.width = width
        obj.height = height
        return obj

    @classmethod
    def from_name(cls, name: str):
        return cls[name.upper()]


class EcodeV1:
    def __init__(self, *,
                 text: str,
                 locale: EcodeLocale = EcodeLocale.JA,
                 flags: AbstractSet[EcodeFlag] = frozenset(),
                 align: EcodeAlign = EcodeAlign.CENTER,
                 size: EcodeSize = EcodeSize.MDPI):
        if not text:
            raise ValueError('empty string is not allowed')

        if not isinstance(locale, EcodeLocale):
            raise ValueError('`locale` must be an instance of `EcodeLocale`, but it is ' + repr(locale))

        if not isinstance(flags, Set):
            raise ValueError('`flags` must be an instance of `Set`, but it is ' + repr(flags))

        self.text = text
        self.locale = locale
        self.flags = flags
        self.align = align
        self.size = size
