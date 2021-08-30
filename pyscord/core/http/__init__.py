# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2021 Pyscord
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Dict, Union

import requests


class HttpApi:
    def __init__(self, version: Union[int, str], token: str) -> None:
        """
        Instantiate a new HttpApi object.

        :param version: The discord API version.
                        See https://discord.com/developers/docs/reference#api-versioning.
        :param token: Discord API token
        """

        self.header = {"Authorization": f"Bot {token}"}
        self.endpoint = f"https://discord.com/api/v{version}"

    def get(self, path) -> Dict:
        """
        :return: JSON response from the discord API.
        """

        res = requests.get(f"{self.endpoint}/{path}", headers=self.header)

        if res.status_code == 200:
            return res.json()
        else:
            raise Exception(res.status_code)
