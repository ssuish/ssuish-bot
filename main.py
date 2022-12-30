import discord
from private import token

client = discord.Bot()

# Create a slash command bot
@client.slash_command(guild_ids=[736241812385038461])
async def hello(ctx):
    await ctx.respond("Hello!")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'{client.user} is connected to the following guilds:\n')
    for guild in client.guilds:
        print(f'{guild.name}(id: {guild.id})')

client.run(token.get_token())