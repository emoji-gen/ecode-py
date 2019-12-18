# -*- encoding: utf-8 -*-

import base64
from typing import List, FrozenSet

from .ecode import (
    EcodeAlign,
    EcodeFlag,
    EcodeFmt,
    EcodeLocale,
    EcodeSize,
    Ecode,
)


class EcodeDecoder:
    @classmethod
    def decode(cls, code: str) -> Ecode:
        code_bytes: bytes = base64.urlsafe_b64decode(cls._pad_base64(code))
        if len(code_bytes) <= Ecode.HEADER_LENGTH:
            raise ValueError('Illegal byte length {}.'.format(len(code_bytes)))

        return Ecode(
            locale=cls._decode_locale(code_bytes[0]),
            flags=cls._decode_flags(code_bytes[1]),
            align=cls._decode_align(code_bytes[1]),
            size=cls._decode_size(code_bytes[2]),
            fmt=cls._decode_fmt(code_bytes[2]),
            font_id=code_bytes[3],
            foreground_color=cls._decode_color(code_bytes[4:8]),
            background_color=cls._decode_color(code_bytes[8:12]),
            text=cls._decode_text(code_bytes[12:])
        )

    @classmethod
    def _pad_base64(cls, s: str):
        return s + '=' * (len(s) % 4)

    @classmethod
    def _decode_locale(cls, byte0: int) -> EcodeLocale:
        locale_id = byte0 & 0x0f
        return EcodeLocale(locale_id)

    @classmethod
    def _decode_flags(cls, byte1: int) -> FrozenSet[EcodeFlag]:
        flags: List[EcodeFlag] = []
        for flag in EcodeFlag:
            if (byte1 >> 2 & 0b0011_1111) & flag.mask:
                flags.append(flag)
        return frozenset(flags)

    @classmethod
    def _decode_align(cls, byte1: int) -> EcodeAlign:
        align_id = byte1 & 0b0000_0011
        return EcodeAlign(align_id)

    @classmethod
    def _decode_size(cls, byte2: int) -> EcodeSize:
        size_id = byte2 >> 4 & 0x0f
        return EcodeSize(size_id)

    @classmethod
    def _decode_fmt(cls, byte2: int) -> EcodeFmt:
        fmt_id = byte2 & 0x0f
        return EcodeFmt(fmt_id)

    @classmethod
    def _decode_color(cls, color: bytes) -> int:
        return color[0] << 24 | color[1] << 16 | color[2] << 8 | color[3]

    @classmethod
    def _decode_text(cls, text: bytes) -> str:
        return text.decode('utf-8')
