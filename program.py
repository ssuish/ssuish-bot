import discord as dc
import logging as log
from owner import Secret

tk = Secret.TOKEN
client = dc.Client()
prefix = "s!"


# client.events
@client.event
async def on_ready():
    print('Logged in as {0.user}' .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello!')

# bot events
@client.event
async def on_guild_join(guild):
    print('Bot has been added to a new server')
    print('List of servers the bot is in: ')

    for guild in client.guilds:
        await print(guild.name)

# Log file
logger = log.getLogger('discord')
logger.setLevel(log.DEBUG)
handler = log.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(log.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client.run(tk)