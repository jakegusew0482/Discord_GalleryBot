import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_NAME = "gallery-submissions"
ALLOWED_FILES = [".png", ".jpg", ".gif"]
DOWNLOAD_DIR = "img"

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

    if message.channel.name == CHANNEL_NAME:
        for attachment in message.attachments:
            extension = attachment.filename[-4:]
            if extension not in ALLOWED_FILES:
                continue

            url = attachment.url
            download_file(DOWNLOAD_DIR, url)


def download_file(directory, url):
    pass


client.run(TOKEN)
