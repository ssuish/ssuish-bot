import discord as dc
import logging as log
from botinfo.token import Secret

client = dc.Client()

class SsuishEvents:    
    prefix = "s!"

    @client.event
    async def on_ready():
        print('Logged in as {0.user}' .format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith(SsuishEvents.prefix + 'hello'):
            await message.channel.send('Hello!')

    @client.event
    async def on_guild_join(guild):
        print('Bot has been added to a new server')
        print('List of servers the bot is in: ')
        for guild in client.guilds:
            await print(guild.name)

class SsuishLogs:
    def log_setup():
        logger = log.getLogger('discord')
        logger.setLevel(log.DEBUG)
        handler = log.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        handler.setFormatter(log.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

class Main:
    def __init__(self):
        Main.main()
        SsuishLogs.log_setup()
        SsuishEvents.on_ready()
        SsuishEvents.on_message()
        SsuishEvents.on_guild_join()
    
    def main():
        tk = Secret.TOKEN
        client.run(tk)
    
if __name__ == '__main__':
    Main.main()