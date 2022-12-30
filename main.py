import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready(message):
    print("We log in as ", client)
    await message.channel.send("I have logged in on the server")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hi")


def get_token():
    try:
        token = os.getenv("TOKEN")
        return token
    except:
        print("Token not found")


client.run(get_token())
