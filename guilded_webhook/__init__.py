import aiohttp
import requests
from datetime import datetime
from typing import List

class Embed:
    def __init__(self, *, title: str=None, description: str=None, url: str=None, color: int=None, timestamp: datetime=None) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.color = int(color)
        self.fields = []
        self.author = {}
        self.footer = {}
        self.timestamp = timestamp
        self.image = {}
        #self.video = {}
        self.thumbnail = {}

    def add_field(self, *, title: str, value: str, inline: bool=False) -> None:
        self.fields.append({"name": title, "value": value, "inline": inline})

    def set_author(self, *, name: str=None, url: str=None, icon_url: str=None) -> None:
        if name:
            self.author["name"] = name
        if url:
            self.author["url"] = url
        if icon_url:
            self.author["iconUrl"] = icon_url

    def set_footer(self, *, text: str, icon_url: str=None) -> None:
        self.footer["text"] = text
        if icon_url:
            self.footer["iconUrl"] = icon_url

    def set_image(self, url: str, height: int=None, width: int=None) -> None:
        self.image["url"] = url
        if height:
            self.image["height"] = height
        if width:
            self.image["width"] = width

    # def set_video(self, url: str, height: int=None, width: int=None) -> None:
    #     self.video["url"] = url
    #     if height:
    #         self.video["height"] = height
    #     if width:
    #         self.video["width"] = width

    def set_thumbnail(self, url: str, height: int=None, width: int=None) -> None:
        self.thumbnail["url"] = url
        if height:
            self.thumbnail["height"] = height
        if width:
            self.thumbnail["width"] = width

    def _to_dict(self) -> dict:
        data = {}
        data["title"] = self.title
        data["description"] = self.description
        data["url"] = self.url
        data["color"] = self.color
        if len(self.fields) != 0:
            data["fields"] = self.fields
        if self.author != {}:
            data["author"] = self.author
        if self.footer != {}:
            data["footer"] = self.footer
        if isinstance(self.timestamp, datetime):
            data["timestamp"] = self.timestamp.isoformat()
        if self.image != {}:
            data["image"] = self.image
        # if self.video != {}:
        #     data["video"] = self.video
        if self.thumbnail != {}:
            data["thumbnail"] = self.thumbnail
        return data

class Webhook:
    def __init__(self, url: str) -> None:
        self.url = url

    def send(self, *, content: str, embeds: List[Embed]) -> None:
        if isinstance(embeds, Embed):
            embeds = [embeds]
        embeds = [embed._to_dict() for embed in embeds]
        requests.post(self.url, json={'content': content, 'embeds': embeds})

class AsyncWebhook:
    def __init__(self, url: str) -> None:
        self.url = url

    async def send(self, *, content: str, embeds: List[Embed]) -> None:
        if isinstance(embeds, Embed):
            embeds = [embeds]
        embeds = [embed._to_dict() for embed in embeds]
        print({'content': content, 'embeds': embeds})
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json={'content': content, 'embeds': embeds}):
                pass
