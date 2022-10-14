import discord as dc
from token import token

client = dc.Client()

class SsuishEvents:    
    prefix = "--"

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

class Main:
    def __init__(self):
        Main.main()
        SsuishEvents.on_ready()
        SsuishEvents.on_message()
        SsuishEvents.on_guild_join()
    
    def main():
        client.run(token())
    
if __name__ == '__main__':
    Main.main()