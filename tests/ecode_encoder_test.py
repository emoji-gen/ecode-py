# -*- encoding: utf-8 -*-

import base64

from ecode import (
    EcodeAlign,
    EcodeFlag,
    EcodeFmt,
    EcodeV1,
    EcodeEncoder,
    EcodeLocale,
    EcodeSize,
)


def test_encode():
    ecode = EcodeV1(
        locale=EcodeLocale.EN,
        flags=frozenset([EcodeFlag.SIZE_FIXED, EcodeFlag.STRETCH]),
        align=EcodeAlign.CENTER,
        size=EcodeSize.XHDPI,
        fmt=EcodeFmt.WEBP,
        font_id=0b11001111,
        foreground_color=0x12345678,
        background_color=0x9abcdef0,
        text='ab\nc'
    )
    code = EcodeEncoder.encode_v1(ecode)
    print('ecode=' + code)  # 'BA0hzxI0VniavN7wYWIKYw'

    actual = base64.urlsafe_b64decode(code + '=' * (len(code) % 4))
    expected = bytes([
        0b00000100,  # Version:4, Locale:4
        0b00001101,  # Flags:6, Align:2
        0b00100001,  # Size:4, Fmt:4
        0b11001111,  # FontId:8
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
    assert actual == expected
