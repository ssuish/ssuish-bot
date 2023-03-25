import discord
from private import token

client = discord.Bot()

# Create a slash command
@client.slash_command(name='test', description='A test command', guild_ids=[530737169682399252, 736241812385038461])
async def test(ctx):
    await ctx.send('Hello World!')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'{client.user} is connected to the following guilds:\n')
    for guild in client.guilds:
        print(f'{guild.name}(id: {guild.id})')

client.run(token.get_token())