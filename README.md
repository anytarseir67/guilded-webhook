# guilded-webhook
 a basic wrapper for guilded's webhooks

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
    hook = guilded.AsyncWebhook('https://media.guilded.gg/webhooks/47871ab2-c998-4289-a440-e0a0186667d9/sRqbvZi4o0uYKQ6AwgSAGYc8cgqu0aC8uAAW2wsWWoy0sOucmsGWgAM0SOKy42a0sQ4uqCmqkOIkO26gMqSA6q')
    embed = guilded.Embed(title="title", description="description", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=0x00ffff, timestamp=datetime.now())
    embed.add_field(title="field title", value="field value")
    embed.set_image("https://img.guildedcdn.com/ContentMedia/e67907d6efa7aebb0440097cb9a03672-Full.webp")
    await hook.send(content='test', embeds=embed)

asyncio.run(main())
```
