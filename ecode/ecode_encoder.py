# -*- encoding: utf-8 -*-

import base64
from typing import AbstractSet

from .ecode import EcodeV1, EcodeFlag


class EcodeEncoder:
    @classmethod
    def encode_v1(cls, ecode: EcodeV1):
        encoded_text = ecode.text.encode('utf-8')
        buff = bytearray(EcodeV1.HEADER_LENGTH + len(encoded_text))

        buff[0] |= ecode.locale.value & 0x0f
        buff[1] |= cls._encode_flags_v1(ecode.flags) << 2 & 0b11111100
        buff[1] |= ecode.align.value & 0x00000011
        buff[2] |= ecode.size.value << 4 & 0xf0
        buff[2] |= ecode.fmt.value & 0x0f
        buff[3] |= ecode.font_id & 0xff
        buff[4] |= ecode.foreground_color >> 24 & 0xff
        buff[5] |= ecode.foreground_color >> 16 & 0xff
        buff[6] |= ecode.foreground_color >> 8 & 0xff
        buff[7] |= ecode.foreground_color & 0xff
        buff[8] |= ecode.background_color >> 24 & 0xff
        buff[9] |= ecode.background_color >> 16 & 0xff
        buff[10] |= ecode.background_color >> 8 & 0xff
        buff[11] |= ecode.background_color & 0xff

        text_bytes = ecode.text.encode('utf-8')
        for (i, c) in enumerate(text_bytes):
            buff[EcodeV1.HEADER_LENGTH + i] = c & 0xff

        return base64.urlsafe_b64encode(buff) \
            .decode('utf-8') \
            .replace('=', '')

    @classmethod
    def _encode_flags_v1(cls, flags: AbstractSet[EcodeFlag]):
        value = 0x00
        for flag in flags:
            value |= 1 << flag.value
        return value
