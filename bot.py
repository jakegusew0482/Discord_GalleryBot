import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

        print(f'{client.user} is connected to:\n'
             f'{guild.name}, ID: {guild.id}'
          )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quote = 'howdy neighbor'

    if message.content == 'howdy':
        await message.channel.send(quote)
client.run(TOKEN)




