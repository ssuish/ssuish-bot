import discord
import os

client = discord.Client()

@client.event
async def on_ready(message):
    print("We log in as ", client)
    await message.channel.send("I have logged in as ", str(client), " and I am ready to go")

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
