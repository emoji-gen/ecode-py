# -*- encoding: utf-8 -*-

from ecode import EcodeAlign


def test_from_code_left():
    assert EcodeAlign.from_code('left') == EcodeAlign.LEFT
    assert EcodeAlign.from_code('Left') == EcodeAlign.LEFT
    assert EcodeAlign.from_code('LEFT') == EcodeAlign.LEFT


def test_from_code_center():
    assert EcodeAlign.from_code('center') == EcodeAlign.CENTER
    assert EcodeAlign.from_code('Center') == EcodeAlign.CENTER
    assert EcodeAlign.from_code('CENTER') == EcodeAlign.CENTER


def test_from_code_right():
    assert EcodeAlign.from_code('right') == EcodeAlign.RIGHT
    assert EcodeAlign.from_code('Right') == EcodeAlign.RIGHT
    assert EcodeAlign.from_code('RIGHT') == EcodeAlign.RIGHT


def test_code():
    assert EcodeAlign.LEFT.code == 'left'
    assert EcodeAlign.CENTER.code == 'center'
    assert EcodeAlign.RIGHT.code == 'right'
