import os
import requests
import discord
import uuid
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('CHANNEL_NAME')
IMG_DIR = os.getenv('IMAGE_DIRECTORY')
ALLOWED_FILES = [".png", ".jpg", ".gif"]

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

    if message.channel.name == CHANNEL:
        for attachment in message.attachments:
            extension = attachment.filename[-4:]
            if extension.upper() not in [x.upper() for x in ALLOWED_FILES]:
                continue

            url = attachment.url
            download_file(url)


def download_file(url):
    extension = url[-4:]
    file = requests.get(url)
    unique_filename = str(uuid.uuid4())
    with open(IMG_DIR + "/" + unique_filename + extension, 'wb') as f:
        f.write(file.content)


client.run(TOKEN)
