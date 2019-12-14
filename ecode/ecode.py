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


class EcodeFmt(IntEnum):
    PNG = 0
    WEBP = 1


class EcodeV1:
    def __init__(self, *,
                 locale: EcodeLocale = EcodeLocale.JA,
                 flags: AbstractSet[EcodeFlag] = frozenset(),
                 align: EcodeAlign = EcodeAlign.CENTER,
                 size: EcodeSize = EcodeSize.MDPI,
                 fmt: EcodeFmt = EcodeFmt.PNG,
                 font_id: int = 0,
                 foreground_color: int = 0x000000FF,
                 background_color: int = 0xFFFFFFFF,
                 text: str):
        if not text:
            raise ValueError('empty string is not allowed')

        if not isinstance(locale, EcodeLocale):
            raise ValueError('`locale` must be an instance of `EcodeLocale`, but it is ' + repr(locale))

        if not isinstance(flags, Set):
            raise ValueError('`flags` must be an instance of `Set`, but it is ' + repr(flags))

        if not isinstance(align, EcodeAlign):
            raise ValueError('`align` must be an instance of `EcodeAlign`, but it is ' + repr(align))

        self.locale = locale
        self.flags = flags
        self.align = align
        self.size = size
        self.fmt = fmt
        self.font_id = font_id
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.text = text
