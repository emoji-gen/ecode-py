# -*- encoding: utf-8 -*-

import pytest

from ecode import Ecode


# noinspection PyTypeChecker
def test_ecode_illegal_locale():
    with pytest.raises(ValueError, match='`locale` must be an instance of `EcodeLocale`, but it is \'xxx\''):
        Ecode(text='ab\nc.', locale='xxx')


# noinspection PyTypeChecker
def test_ecode_illegal_flags():
    with pytest.raises(ValueError, match='`flags` must be an instance of `Set`, but it is \'flags\''):
        Ecode(text='ab\nc', flags='flags')


# noinspection PyTypeChecker
def test_ecode_illegal_flag_contents():
    with pytest.raises(ValueError,
                       match='`flags` must include instances of `EcodeFlag` only, but \'flag\' is contained'):
        Ecode(text='ab\nc', flags=frozenset(['flag']))


# noinspection PyTypeChecker
def test_ecode_illegal_align():
    with pytest.raises(ValueError, match='`align` must be an instance of `EcodeAlign`, but it is \'align\''):
        Ecode(text='ab\nc', align='align')


# noinspection PyTypeChecker
def test_ecode_illegal_size():
    with pytest.raises(ValueError, match='`size` must be an instance of `EcodeSize`, but it is \'size\''):
        Ecode(text='ab\nc', size='size')


# noinspection PyTypeChecker
def test_ecode_illegal_fmt():
    with pytest.raises(ValueError, match='`fmt` must be an instance of `EcodeFmt`, but it is \'fmt\''):
        Ecode(text='ab\nc', fmt='fmt')


def test_ecode_illegal_foreground_color():
    with pytest.raises(ValueError,
                       match='`foreground_color` must be between 0 and 0xFFFFFFFF, but it is ' + repr(0xFFFFFFFF + 1)):
        Ecode(text='ab\nc', foreground_color=0xFFFFFFFF + 1)


def test_ecode_illegal_background_color():
    with pytest.raises(ValueError,
                       match='`background_color` must be between 0 and 0xFFFFFFFF, but it is ' + repr(0xFFFFFFFF + 1)):
        Ecode(text='ab\nc', background_color=0xFFFFFFFF + 1)


def test_encode_empty_text():
    with pytest.raises(ValueError, match='empty string is not allowed'):
        Ecode(text='')
