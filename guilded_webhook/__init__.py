import aiohttp
import requests
import json

from .embed import Embed
from .file import File
from . import exceptions

from typing import List, Union

class Empty:
    ...

class BaseWebHook:
    __slots__ = ("_url", "avatar", "username")

    def __init__(self, url: str, *, avatar: str=None, username: str=None) -> None:
        self._url = url
        self.avatar = avatar
        self.username = username

    def __repr__(self) -> str:
        return self._url

    def __eq__(self, o: object) -> bool:
        if isinstance(o, BaseWebHook):
            return self._url == o._url
        return False

class Webhook(BaseWebHook):
    """Class implementing a syncronous webhook
    
    Parameters
    ----------
    url : str
        The webhook url to POST to.
    avatar : str, optional
        when present, overrides the avatar set on guilded, by default None
    username : str, optional
        when present, overrides the username set on guilded, by default None

    Attributes
    -----------
    avatar: :class:`str`
        The override avatar set in the constructor
    username: :class:`str`
        The override username set in the constructor
    """
    def send(self, *, content: str=None, embeds: Union[List[Embed], Embed]=None, avatar: str=Empty, username: str=Empty, file: File=None) -> None:
        """method to send a message to the webhook. `avatar`and `username` are overrides for the :class:`Webhook` instance's overrides, passing None disables them, leaving blank uses them as is, passing a value overrides them.

        Parameters
        ----------
        content : str, optional
            text to send
        embeds : Union[List[Embed], Embed], optional
            embed, or list of embeds to send
        avatar : str, optional
            override avatar
        username : str, optional
            override username
        file : File, optional
            file to send attached to the message, by default None

        Raises
        ------
        exceptions.BadRequestError
            raised when the response contains an error code
        """
        raw_json = {'content': content}
        if avatar == Empty:
            avatar = self.avatar
        if avatar != None:
            raw_json['avatar_url'] = avatar

        if username == Empty:
            username = self.username
        if username != None:
            raw_json['username'] = username

        if embeds:
            if isinstance(embeds, Embed):
                embeds = [embeds]
            _embeds = [embed._to_dict() for embed in embeds]
            raw_json['embeds'] = _embeds

        if file:
            form = {
                'payload_json': (None, json.dumps(raw_json), 'application/json'),
                'files[0]': (file.filename, file.read(), file.content_type)
            }
            r = requests.post(self._url, files=form)
        else:
            r = requests.post(self._url, json=raw_json)

        resp = r.json()
        if 'code' in resp:
            raise exceptions.BadRequestError(resp['message'])

class AsyncWebhook(BaseWebHook):
    """Class implementing an asyncronous webhook
    
    Parameters
    ----------
    url : str
        The webhook url to POST to.
    avatar : str, optional
        when present, overrides the avatar set on guilded, by default None
    username : str, optional
        when present, overrides the username set on guilded, by default None

    Attributes
    -----------
    avatar: :class:`str`
        The override avatar set in the constructor
    username: :class:`str`
        The override username set in the constructor
    """
    async def send(self, *, content: str=None, embeds: Union[List[Embed], Embed]=None, avatar: str=Empty, username: str=Empty, file: File=None) -> None:
        """method to send a message to the webhook. `avatar`and `username` are overrides for the :class:`AsyncWebhook` instance's overrides, passing None disables them, leaving blank uses them as is, passing a value overrides them.

        Parameters
        ----------
        content : str, optional
            text to send
        embeds : Union[List[Embed], Embed], optional
            embed, or list of embeds to send
        avatar : str, optional
            override avatar
        username : str, optional
            override username
        file : File, optional
            file to send attached to the message, by default None

        Raises
        ------
        exceptions.BadRequestError
            raised when the response contains an error code
        """
        raw_json = {'content': content}
        if avatar == Empty:
            avatar = self.avatar
        if avatar != None:
            raw_json['avatar_url'] = avatar

        if username == Empty:
            username = self.username
        if username != None:
            raw_json['username'] = username

        if embeds:
            if isinstance(embeds, Embed):
                embeds = [embeds]
            _embeds = [embed._to_dict() for embed in embeds]
            raw_json['embeds'] = _embeds

        if file:
            data = aiohttp.FormData()
            enc = json.dumps(raw_json)
            data.add_field('payload_json', enc, content_type="application/json")
            data.add_field("files[0]", file.read(), filename=file.filename, content_type=file.content_type)

            async with aiohttp.ClientSession() as session:
                async with session.post(self._url, data=data) as r:
                    resp = await r.json()
        else:
            async with aiohttp.ClientSession() as session:
                async with session.post(self._url, json=raw_json) as r:
                    resp = await r.json()

        if 'code' in resp:
            raise exceptions.BadRequestError(resp['message'])