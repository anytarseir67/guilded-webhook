import aiohttp
import requests
from datetime import datetime
from typing import List, Dict, Union, Any
class Embed:
    __slots__ = ("_title", "_description", "_url", "_color", "_fields", "_author", "_footer", "_timestamp", "_image", "_thumbnail")
    def __init__(self, *, title: str=None, description: str=None, url: str=None, color: int=None, timestamp: datetime=None) -> None:
        self._title = title
        self._description = description
        self._url = url
        self._color = color
        self._fields: List[Dict[str, Union[str,bool]]] = [] 
        self._author: Dict[str, str] = {}
        self._footer: Dict[str, str] = {}
        self._timestamp = timestamp
        self._image: Dict[str, Union[str, int]] = {}
        #self._video: Dict[str, Union[str, int]] = {}
        self._thumbnail: Dict[str, Union[str, int]] = {}

    def add_field(self, *, title: str, value: str, inline: bool=False) -> None:
        self._fields.append({"name": title, "value": value, "inline": inline})

    def set_author(self, *, name: str=None, url: str=None, icon_url: str=None) -> None:
        if name:
            self._author["name"] = name
        if url:
            self._author["url"] = url
        if icon_url:
            self._author["iconUrl"] = icon_url

    def set_footer(self, *, text: str, icon_url: str=None) -> None:
        self._footer["text"] = text
        if icon_url:
            self._footer["iconUrl"] = icon_url

    def set_image(self, url: str, height: int=None, width: int=None) -> None:
        self._image["url"] = url
        if height:
            self._image["height"] = height
        if width:
            self._image["width"] = width

    # def set_video(self, url: str, height: int=None, width: int=None) -> None:
    #     self._video["url"] = url
    #     if height:
    #         self._video["height"] = height
    #     if width:
    #         self._video["width"] = width

    def set_thumbnail(self, url: str, height: int=None, width: int=None) -> None:
        self._thumbnail["url"] = url
        if height:
            self._thumbnail["height"] = height
        if width:
            self._thumbnail["width"] = width

    def _to_dict(self) -> dict:
        data: Dict[Any, Any] = {}
        data["title"] = self._title
        data["description"] = self._description
        data["url"] = self._url
        data["color"] = self._color
        if len(self._fields) != 0:
            data["fields"] = self._fields
        if self._author != {}:
            data["author"] = self._author
        if self._footer != {}:
            data["footer"] = self._footer
        if isinstance(self._timestamp, datetime):
            data["timestamp"] = self._timestamp.isoformat()
        if self._image != {}:
            data["image"] = self._image
        # if self._video != {}:
        #     data["video"] = self._video
        if self._thumbnail != {}:
            data["thumbnail"] = self._thumbnail
        return data

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
