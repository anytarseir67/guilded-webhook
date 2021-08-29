# guilded-webhook
## a basic wrapper for guilded's webhooks

Basic example:

```
import guilded_webhook as guilded
import asyncio

async def main():
    hook = guilded.AsyncWebhook('https://media.guilded.gg/webhooks/REDACTED')
    await hook.send(content='test')

asyncio.run(main())
```

or

```
import guilded_webhook as guilded

def main():
    hook = guilded.Webhook('https://media.guilded.gg/webhooks/REDACTED')
    hook.send(content='test')

main()
```

guilded-webhook also supports embeds (heavily inspired by discord.py's embeds)
```
import guilded_webhook as guilded
import asyncio
from datetime import datetime

async def main():
    hook = guilded.AsyncWebhook('https://media.guilded.gg/webhooks/REDACTED')
    embed = guilded.Embed(title="title", description="description", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=0x00ffff, timestamp=datetime.now())
    embed.add_field(title="field title", value="field value")
    embed.set_image("https://img.guildedcdn.com/ContentMedia/e67907d6efa7aebb0440097cb9a03672-Full.webp")
    await hook.send(content='test', embeds=embed)

asyncio.run(main())
```
# docs
## class - AsyncWebHook
* ### (async) method - send 
  * ####  (kwarg) string - content
  * #### (kwarg) List[Embed] - embeds

## class - WebHook
* ### method - send 
  * ####  (kwarg) string - content
  * #### (kwarg) List[Embed] - embeds

## class - Embed
* ### (kwarg) str - title
* ### (kwarg) str - description
* ### (kwarg) str - url
* ### (kwarg) int - color (hex color)
* ### (kwarg) datetime.datetime - timestamp
* ### method - add_field
  * #### (kwarg) str - title
  * #### (kwarg) str - value
  * #### (kwarg) bool - inline
* ### method - set_author
  * #### (kwarg) str - name
  * #### (kwarg) str - url
  * #### (kwarg) str - icon_url
* ### method - set_footer
  * #### (kwarg) str - text
  * #### (kwarg) str - icon_url
* ### method - set_image
  * #### (kwarg) str - url
  * #### (kwarg) int - height
  * #### (kwarg) int - width
* ### method - set_thumbnail
  * #### (kwarg) str - url
  * #### (kwarg) int - height
  * #### (kwarg) int - width