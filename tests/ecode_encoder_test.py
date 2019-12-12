# -*- encoding: utf-8 -*-

import pytest

from ecode import (
    EcodeV1,
    EcodeEncoder,
    EcodeLocale,
)


def test_encode():
    ecode = EcodeV1(
        locale=EcodeLocale.EN,
        text='abc',
    )
    code = EcodeEncoder.encode(ecode)
    print(code)

    # print(ecode_encoder.encode({
    #     'text': 'abc',
    #     'locale': 'en',
    # }))
    # assert False


# noinspection PyTypeChecker
def test_encode_illegal_locale():
    with pytest.raises(ValueError, match='`locale` must be an instance of `EcodeLocale`, but it is \'xxx\''):
        EcodeV1(text='ab\nc.', locale='xxx')
