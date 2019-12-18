# ecode-py
[![Build Status](https://travis-ci.com/emoji-gen/ecode-py.svg?branch=master)](https://travis-ci.com/emoji-gen/ecode-py)

:musical_score: The emoji code utilities for Python

## Requirements

- Python 3.6 or later

## Getting started

```shell script
$ pip install ecode
```

## Usage
### Encoding

```python
from ecode import *

ecode = Ecode(
    locale=EcodeLocale.EN,
    flags=frozenset(EcodeFlag.SIZE_FIXED, EcodeFlag.STRETCH),
    align=EcodeAlign.CENTER,
    size=EcodeSize.XHDPI,
    format=EcodeFmt.WEBP,
    font_id=0xcf,
    foreground_color=0x12345678,
    background_color=0x9abcdef0,
    text='ab\nc')


code = EcodeEncoder.encode(ecode)
print(code) # => 'BA0hzxI0VniavN7wYWIKYw'
```

### Decoding

```python
from ecode import EcodeDecoder

ecode = EcodeDecoder.decode('BA0hzxI0VniavN7wYWIKYw')
print(ecode.text) # => 'ab\nc'
```

## Development
### Requirements

```shell script
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
```

### Test

```shell script
$ pytest
```

### Publish

TODO

## Ported projects

|Name|Language|
|---|---|
|[ecode-java](https://github.com/emoji-gen/ecode-java)|Java|
|[ecode-js](https://github.com/emoji-gen/ecode-js)|JavaScript|
|[ecode-py](https://github.com/emoji-gen/ecode-py)|Python|

## License

MIT &copy; [Emoji Generator](https://emoji-gen.ninja)

