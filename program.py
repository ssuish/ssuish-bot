from asyncio import proactor_events
import discord as dc

from private import Secret

tk = Secret().get_token()

client = dc.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}' .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(tk)