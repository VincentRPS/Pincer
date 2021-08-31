# Pincer

<!--
[![PyPI - Downloads](https://img.shields.io/badge/dynamic/json?label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2FPincer)](https://pypi.org/project/Pincer)
![PyPI](https://img.shields.io/pypi/v/Pincer)
![PyPI - Format](https://img.shields.io/pypi/format/Pincer)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Pincer)
-->

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Pincer-org/pincer/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/Pincer-org/pincer/?branch=main)
[![Build Status](https://scrutinizer-ci.com/g/Pincer-org/Pincer/badges/build.png?b=main)](https://scrutinizer-ci.com/g/Pincer-org/Pincer/build-status/main)
![GitHub repo size](https://img.shields.io/github/repo-size/Pincer-org/Pincer)
![GitHub last commit](https://img.shields.io/github/last-commit/Pincer-org/Pincer)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Pincer-org/Pincer)
![GitHub](https://img.shields.io/github/license/Pincer-org/Pincer)
![Code Style](https://img.shields.io/badge/code%20style-pep8-green)
![Discord](https://img.shields.io/discord/881531065859190804)

*An asynchronous python API wrapper meant to replace discord.py*

# The package is currently within the planning phase

## 📌 Links

> Join the discord server: https://discord.gg/8WkYz3fNFm

> The pypi package: https://pypi.org/project/Pincer/

> Our website: https://pincer.dev


## ☄️ Installation

Use the following command to install Pincer into your python environment:

```bash
pip install pincer
```

<details>
	<summary>
		⚙️ <i> Didn't work?</i>
	</summary>

Depending on your python installation, you might need to use one of the following.

*pip isn't in the path but python is*
```sh
python -m pip install pincer
```

*Unix system can use pip3/python3 command*
```sh
python3 -m pip install pincer
```

```sh
pip3 install pincer
```

*python isn't in the path*
```sh
path/to/python.exe -m pip install pincer
```

*Using multiple python versions*
```sh
py -m pip install pincer
```
</details>

## Current Features
- Dispatcher
- Logging
- `New` HTTP Client

**HTTP client example**: *Adding a reaction to a message*
```py
import asyncio

from pincer.core.http import HTTPClient

client = HTTPClient("...")

CHANNEL_ID: int = ...
MESSAGE_ID: int = ...
REACTION: str = ...
# see: https://discord.com/developers/docs/resources/channel#get-channel


async def add_reaction() -> None:
    await client.put(
        f'channels/{CHANNEL_ID}/messages/{MESSAGE_ID}/reactions/{REACTION}/@me',
        {}
    )


def main() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(add_reaction())


if __name__ == '__main__':
    main()

```

## 🏷️ License

`© 2021 copyright Pincer`

This repository is licensed under the MIT License.

See LICENSE for details.