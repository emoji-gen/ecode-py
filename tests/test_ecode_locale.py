# -*- encoding: utf-8 -*-

from ecode import EcodeLocale


def test_from_code_ja():
    assert EcodeLocale.from_code('ja') == EcodeLocale.JA
    assert EcodeLocale.from_code('Ja') == EcodeLocale.JA
    assert EcodeLocale.from_code('JA') == EcodeLocale.JA


def test_from_code_ko():
    assert EcodeLocale.from_code('ko') == EcodeLocale.KO


def test_from_code_zh_hans():
    assert EcodeLocale.from_code('zh') == EcodeLocale.ZH_HANS
    assert EcodeLocale.from_code('zh-hans') == EcodeLocale.ZH_HANS
    assert EcodeLocale.from_code('zh_hans') == EcodeLocale.ZH_HANS


def test_from_code_zh_hant():
    assert EcodeLocale.from_code('zh-hant') == EcodeLocale.ZH_HANT
    assert EcodeLocale.from_code('zh_hant') == EcodeLocale.ZH_HANT


def test_from_code_en():
    assert EcodeLocale.from_code('en') == EcodeLocale.EN


def test_code():
    assert EcodeLocale.JA.code == 'ja'
    assert EcodeLocale.KO.code == 'ko'
    assert EcodeLocale.ZH_HANS.code == 'zh-Hans'
    assert EcodeLocale.ZH_HANT.code == 'zh-Hant'
    assert EcodeLocale.EN.code == 'en'
