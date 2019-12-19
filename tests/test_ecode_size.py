# -*- encoding: utf-8 -*-

from ecode import EcodeSize


def test_from_code():
    assert EcodeSize.from_code('mdpi') == EcodeSize.MDPI
    assert EcodeSize.from_code('Mdpi') == EcodeSize.MDPI
    assert EcodeSize.from_code('MDPI') == EcodeSize.MDPI


def test_code():
    assert EcodeSize.MDPI.code == 'mdpi'
    assert EcodeSize.HDPI.code == 'hdpi'
    assert EcodeSize.XHDPI.code == 'xhdpi'
    assert EcodeSize.XXHDPI.code == 'xxhdpi'
