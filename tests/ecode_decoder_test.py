# -*- encoding: utf-8 -*-

from ecode import (
    EcodeAlign,
    EcodeDecoder,
    EcodeFlag,
    EcodeFmt,
    EcodeLocale,
    EcodeSize,
)


def test_decode():
    ecode = EcodeDecoder.decode_v1('BA0hzxI0VniavN7wYWIKYw')
    assert ecode.version == 1
    assert ecode.locale == EcodeLocale.EN
    assert ecode.flags == frozenset([EcodeFlag.SIZE_FIXED, EcodeFlag.STRETCH])
    assert ecode.align == EcodeAlign.CENTER
    assert ecode.size == EcodeSize.XHDPI
    assert ecode.fmt == EcodeFmt.WEBP
    assert ecode.font_id == 0b11001111
    assert ecode.foreground_color == 0x12345678
    assert ecode.background_color == 0x9abcdef0
