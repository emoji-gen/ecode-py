# ecode-py
[![Build Status](https://travis-ci.com/emoji-gen/ecode-py.svg?branch=master)](https://travis-ci.com/emoji-gen/ecode-py)
[![codecov](https://codecov.io/gh/emoji-gen/ecode-py/branch/master/graph/badge.svg)](https://codecov.io/gh/emoji-gen/ecode-py)
[![Requirements Status](https://requires.io/github/emoji-gen/ecode-py/requirements.svg?branch=master)](https://requires.io/github/emoji-gen/ecode-py/requirements/?branch=master)

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
    text='ab\nc'
)


code = EcodeEncoder.encode(ecode)
print(code) #=> 'BA0hzxI0VniavN7wYWIKYw'
```

### Decoding

```python
from ecode import EcodeDecoder

ecode = EcodeDecoder.decode('BA0hzxI0VniavN7wYWIKYw')
print(ecode.text) #=> 'ab\nc'
```

## Development
### Install requirements

```shell script
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
```

### Upgrade requirements

```shell script
$ ./scripts/upgrade-requirements-dev.sh
```

### Test

```shell script
$ . venv/bin/activate
$ pytest
```

### Publish


```shell script
$ ./scripts/publish-pypi.sh
```

## Ported projects

|Name|Language|
|---|---|
|[ecode-java](https://github.com/emoji-gen/ecode-java)|Java|
|[ecode-js](https://github.com/emoji-gen/ecode-js)|JavaScript|
|[ecode-py](https://github.com/emoji-gen/ecode-py)|Python|

## License

MIT &copy; [Emoji Generator](https://emoji-gen.ninja)

