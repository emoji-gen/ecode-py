# -*- encoding: utf-8 -*-

import base64


V1_HEADER_LENGTH = 12
class EcodeEncoder():
    def encode(self, ecode):
        encoded_text = ecode.text.encode('utf-8')
        buff = bytearray(V1_HEADER_LENGTH + len(encoded_text))

        buff[0] |= ecode.locale.value & 0x0f

        print(buff)
        return base64.urlsafe_b64encode(buff)
