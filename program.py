from asyncio import proactor_events
import discord as dc
import logging as log
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

# Log file
logger = log.getLogger('discord')
logger.setLevel(log.DEBUG)
handler = log.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(log.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client.run(tk)