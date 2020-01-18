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


def test_width():
    assert EcodeSize.MDPI.width == 128
    assert EcodeSize.HDPI.width == 192
    assert EcodeSize.XHDPI.width == 256
    assert EcodeSize.XXHDPI.width == 384


def test_height():
    assert EcodeSize.MDPI.height == 128
    assert EcodeSize.HDPI.height == 192
    assert EcodeSize.XHDPI.height == 256
    assert EcodeSize.XXHDPI.height == 384
