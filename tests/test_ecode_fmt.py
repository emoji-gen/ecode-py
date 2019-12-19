# -*- encoding: utf-8 -*-

from ecode import EcodeFmt


def test_from_code_png():
    assert EcodeFmt.from_code('png') == EcodeFmt.PNG
    assert EcodeFmt.from_code('Png') == EcodeFmt.PNG
    assert EcodeFmt.from_code('PNG') == EcodeFmt.PNG


def test_from_code_webp():
    assert EcodeFmt.from_code('webp') == EcodeFmt.WEBP
    assert EcodeFmt.from_code('WebP') == EcodeFmt.WEBP
    assert EcodeFmt.from_code('WEBP') == EcodeFmt.WEBP


def test_code():
    assert EcodeFmt.PNG.code == 'png'
    assert EcodeFmt.WEBP.code == 'webp'
