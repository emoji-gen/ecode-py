# -*- encoding: utf-8 -*-

from ecode import EcodeEncoder

def test_encode():
    ecode_encoder = EcodeEncoder()
    print(ecode_encoder.encode({
        'text': 'abc',
        'locale': 'en',
    }))
    assert False
