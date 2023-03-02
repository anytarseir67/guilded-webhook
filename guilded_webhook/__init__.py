import aiohttp
import requests
from typing import List, Union
from .embed import Embed
from .exceptions import BadRequestError

class Empty:
    ...

class Webhook:
    __slots__ = ("_url", "avatar", "username")
    def __init__(self, url: str, *, avatar: str=None, username: str=None) -> None:
        self._url = url
        self.avatar = avatar
        self.username = username

    def __repr__(self) -> str:
        return self._url

    def __eq__(self, o: object) -> bool:
        if isinstance(o, (AsyncWebhook, Webhook)):
            return self._url == o._url
        return False

    def send(self, *, content: str=None, embeds: Union[List[Embed], Embed]=None, avatar: str=Empty, username: str=Empty) -> None:
        json = {'content': content}
        if avatar == Empty:
            avatar = self.avatar
        if avatar != None:
            json['avatar_url'] = avatar

        if username == Empty:
            username = self.username
        if username != None:
            json['username'] = username

        if embeds:
            if isinstance(embeds, Embed):
                embeds = [embeds]
            _embeds = [embed._to_dict() for embed in embeds]
            json['embed'] = _embeds

        r = requests.post(self._url, json=json)
        resp = r.json()

        if 'code' in resp:
            raise BadRequestError(resp['message'])

class AsyncWebhook:
    __slots__ = ("_url", "avatar", "username")
    def __init__(self, url: str) -> None:
        self._url = url

    def __repr__(self) -> str:
        return self._url

    def __eq__(self, o: object) -> bool:
        if isinstance(o, (AsyncWebhook, Webhook)):
            return self._url == o._url
        return False

    async def send(self, *, content: str=None, embeds: Union[List[Embed], Embed]=None, avatar: str=Empty, username: str=Empty) -> None:
        json = {'content': content}
        if avatar == Empty:
            avatar = self.avatar
        if avatar != None:
            json['avatar_url'] = avatar

        if username == Empty:
            username = self.username
        if username != None:
            json['username'] = username

        if embeds:
            if isinstance(embeds, Embed):
                embeds = [embeds]
            _embeds = [embed._to_dict() for embed in embeds]
            json['embed'] = _embeds

        async with aiohttp.ClientSession() as session:
            async with session.post(self._url, json=json) as r:
                resp = await r.json()

        if 'code' in resp:
            raise BadRequestError(resp['message'])