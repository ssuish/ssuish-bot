import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("We log in as ", client)

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