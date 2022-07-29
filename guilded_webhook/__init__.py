import aiohttp
import requests
from typing import List, Union
from .embed import Embed

class Webhook:
    __slots__ = ("_url")
    def __init__(self, url: str) -> None:
        self._url = url

    def __repr__(self) -> str:
        return self._url

    def __eq__(self, o: object) -> bool:
        if isinstance(o, (AsyncWebhook, Webhook)):
            return self._url == o._url
        return False

    def send(self, *, content: str=None, embeds: Union[List[Embed], Embed]=None) -> None:
        if embeds:
            if isinstance(embeds, Embed):
                embeds = [embeds]
            _embeds = [embed._to_dict() for embed in embeds]
            requests.post(self._url, json={'content': content, 'embeds': _embeds})
            return
        else:
            requests.post(self._url, json={'content': content})
            return

class AsyncWebhook:
    __slots__ = ("_url")
    def __init__(self, url: str) -> None:
        self._url = url

    def __repr__(self) -> str:
        return self._url

    def __eq__(self, o: object) -> bool:
        if isinstance(o, (AsyncWebhook, Webhook)):
            return self._url == o._url
        return False

    async def send(self, *, content: str=None, embeds: Union[List[Embed], Embed]=None) -> None:
        async with aiohttp.ClientSession() as session:
            if embeds:
                if isinstance(embeds, Embed):
                    embeds = [embeds]
                _embeds = [embed._to_dict() for embed in embeds]
                async with session.post(self._url, json={'content': content, 'embeds': _embeds}):
                    return
            else:
                async with session.post(self._url, json={'content': content}):
                    return
