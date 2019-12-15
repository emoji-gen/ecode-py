# -*- encoding: utf-8 -*-

import pytest

from ecode import EcodeV1


# noinspection PyTypeChecker
def test_ecode_illegal_locale():
    with pytest.raises(ValueError, match='`locale` must be an instance of `EcodeLocale`, but it is \'xxx\''):
        EcodeV1(text='ab\nc.', locale='xxx')


# noinspection PyTypeChecker
def test_ecode_illegal_flags():
    with pytest.raises(ValueError, match='`flags` must be an instance of `Set`, but it is \'flags\''):
        EcodeV1(text='ab\nc', flags='flags')


# noinspection PyTypeChecker
def test_ecode_illegal_align():
    with pytest.raises(ValueError, match='`align` must be an instance of `EcodeAlign`, but it is \'align\''):
        EcodeV1(text='ab\nc', align='align')


# noinspection PyTypeChecker
def test_ecode_illegal_size():
    with pytest.raises(ValueError, match='`size` must be an instance of `EcodeSize`, but it is \'size\''):
        EcodeV1(text='ab\nc', size='size')


# noinspection PyTypeChecker
def test_ecode_illegal_fmt():
    with pytest.raises(ValueError, match='`fmt` must be an instance of `EcodeFmt`, but it is \'fmt\''):
        EcodeV1(text='ab\nc', fmt='fmt')


def test_ecode_illegal_foreground_color():
    with pytest.raises(ValueError,
                       match='`foreground_color` must be bellow 0xFFFFFFFF, but it is ' + repr(0xFFFFFFFF + 1)):
        EcodeV1(text='ab\nc', foreground_color=0xFFFFFFFF + 1)


def test_encode_empty_text():
    with pytest.raises(ValueError, match='empty string is not allowed'):
        EcodeV1(text='')
