# -*- encoding: utf-8 -*-

from ecode import EcodeFlag


def test_from_code():
    assert EcodeFlag.from_code('size_fixed') == EcodeFlag.SIZE_FIXED
    assert EcodeFlag.from_code('SIZE_FIXED') == EcodeFlag.SIZE_FIXED
    assert EcodeFlag.from_code('stretch') == EcodeFlag.STRETCH
    assert EcodeFlag.from_code('STRETCH') == EcodeFlag.STRETCH


def test_mask():
    assert EcodeFlag.SIZE_FIXED.mask == 0b0000_0001
    assert EcodeFlag.STRETCH.mask == 0b0000_0010
