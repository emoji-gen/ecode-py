# -*- encoding: utf-8 -*-

import base64


V1_HEADER_LENGTH = 12
LOCALE_NAME_TO_LOCALE_ID = {
    'ja': 0,
    'kr': 1,
    'zh-hant': 2,
    'zh-hans': 3,
    'en': 4,
}


class EcodeEncoder():
    def encode(self, ecode):
        text = ecode.get('text')
        if not text:
            raise ValueError('empty string is not allowed')

        encoded_text = text.encode('utf-8')
        buff = bytearray(V1_HEADER_LENGTH + len(encoded_text))

        locale_name = ecode.get('locale', 'ja')
        locale_id = LOCALE_NAME_TO_LOCALE_ID.get(locale_name.lower())
        if locale_id is None:
            raise ValueError('Illegal locale name : ' + ecode.get('locale'))
        buff[0] |= locale_id & 0x0f


        print(buff)
        return base64.urlsafe_b64encode(buff)
