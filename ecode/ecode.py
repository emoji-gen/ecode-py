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
    def from_code(cls, code: str) -> 'EcodeLocale':
        upper_code = code.upper()
        if upper_code == 'ZH':
            return cls.ZH_HANS

        return cls[upper_code.replace('-', '_')]

    @property
    def code(self) -> str:
        if self == EcodeLocale.ZH_HANT:
            return 'zh-Hant'
        if self == EcodeLocale.ZH_HANS:
            return 'zh-Hans'
        return self.name.lower()


@enum.unique
class EcodeFlag(IntEnum):
    SIZE_FIXED = 0
    STRETCH = 1

    @classmethod
    def from_code(cls, code: str) -> 'EcodeFlag':
        return cls[code.upper()]

    @property
    def code(self) -> str:
        return self.name.lower()

    @property
    def mask(self) -> int:
        return 1 << self.value


@enum.unique
class EcodeAlign(IntEnum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2

    @classmethod
    def from_code(cls, code: str) -> 'EcodeAlign':
        return cls[code.upper()]

    @property
    def code(self) -> str:
        return self.name.lower()


@enum.unique
class EcodeSize(IntEnum):
    MDPI = 0
    HDPI = 1
    XHDPI = 2
    XXHDPI = 3

    @classmethod
    def from_code(cls, code: str) -> 'EcodeSize':
        return cls[code.upper()]

    @property
    def code(self) -> str:
        return self.name.lower()


class EcodeFmt(IntEnum):
    PNG = 0
    WEBP = 1

    @classmethod
    def from_code(cls, code: str) -> 'EcodeFmt':
        return cls[code.upper()]

    @property
    def code(self) -> str:
        return self.name.lower()


class Ecode:
    HEADER_LENGTH = 12

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
        if not isinstance(locale, EcodeLocale):
            raise ValueError('`locale` must be an instance of `EcodeLocale`, but it is {!r}'.format(locale))

        if not isinstance(flags, Set):
            raise ValueError('`flags` must be an instance of `Set`, but it is ' + repr(flags))

        for flag in flags:
            if not isinstance(flag, EcodeFlag):
                raise ValueError('`flags` must include instances of `EcodeFlag` only, ' +
                                 'but {} is contained'.format(repr(flag)))

        if not isinstance(align, EcodeAlign):
            raise ValueError('`align` must be an instance of `EcodeAlign`, but it is ' + repr(align))

        if not isinstance(size, EcodeSize):
            raise ValueError('`size` must be an instance of `EcodeSize`, but it is ' + repr(size))

        if not isinstance(fmt, EcodeFmt):
            raise ValueError('`fmt` must be an instance of `EcodeFmt`, but it is ' + repr(fmt))

        if foreground_color & 0xFFFFFFFF != foreground_color:
            raise ValueError('`foreground_color` must be between 0 and 0xFFFFFFFF, but it is ' + repr(foreground_color))

        if background_color & 0xFFFFFFFF != background_color:
            raise ValueError('`background_color` must be between 0 and 0xFFFFFFFF, but it is ' + repr(background_color))

        if not text:
            raise ValueError('empty string is not allowed')

        self.locale = locale
        self.flags = flags
        self.align = align
        self.size = size
        self.fmt = fmt
        self.font_id = font_id
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.text = text

    @property
    def version(self) -> int:
        return 1
