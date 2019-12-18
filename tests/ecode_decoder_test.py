# -*- encoding: utf-8 -*-

import pytest

from base64 import urlsafe_b64encode

from ecode import (
    EcodeAlign,
    EcodeDecoder,
    EcodeFlag,
    EcodeFmt,
    EcodeLocale,
    EcodeSize,
)


def test_decode():
    ecode = EcodeDecoder.decode('BA0hzxI0VniavN7wYWIKYw')
    assert ecode.version == 1
    assert ecode.locale == EcodeLocale.EN
    assert ecode.flags == frozenset([EcodeFlag.SIZE_FIXED, EcodeFlag.STRETCH])
    assert ecode.align == EcodeAlign.CENTER
    assert ecode.size == EcodeSize.XHDPI
    assert ecode.fmt == EcodeFmt.WEBP
    assert ecode.font_id == 0b1100_1111
    assert ecode.foreground_color == 0x12345678
    assert ecode.background_color == 0x9abcdef0
    assert ecode.text == 'ab\nc'


def test_decode_illegal_locale():
    code_bytes = bytes([
        0b0000_1111,  # Version:4, Locale:4
        0b0000_1101,  # Flags:6, Align:2
        0b0010_0001,  # Size:4, Fmt:4
        0b1100_1111,  # FontId:8
        0x12,  # ForegroundColor_R:8
        0x34,  # ForegroundColor_G:8
        0x56,  # ForegroundColor_B:8
        0x78,  # ForegroundColor_A:8
        0x9a,  # BackgroundColor_R:8
        0xbc,  # BackgroundColor_G:8
        0xde,  # BackgroundColor_B:8
        0xf0,  # BackgroundColor_A:8
        0x61,  # Text:8,
        0x62,  # Text:8
        0x0a,  # Text:8
        0x63,  # Text:8
    ])
    code = urlsafe_b64encode(code_bytes).decode('utf-8')

    with pytest.raises(ValueError, match='EcodeLocale'):
        EcodeDecoder.decode(code)
