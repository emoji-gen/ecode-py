# -*- encoding: utf-8 -*-

import pytest

from ecode import EcodeV1, EcodeEncoder

def test_encode():
    ecode = EcodeV1(
        text='abc',
    )
    code = EcodeEncoder().encode(ecode)
    print(code)

    # print(ecode_encoder.encode({
    #     'text': 'abc',
    #     'locale': 'en',
    # }))
    assert False

# def test_encode_illegal_locale():
#     with pytest.raises(ValueError, match='Illegal locale name : xxx'):
#         EcodeEncoder().encode({
#             'text': 'abc',
#             'locale': 'xxx',
#         })
