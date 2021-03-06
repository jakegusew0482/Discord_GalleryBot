import os
import requests
import discord
import uuid
import re
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

    match = re.search(r"((i|I)'*( *(a|A))*(m|M))( )+(.+)", message.content)
    if match:
        await message.channel.send("Hi %s." % match.group(7))

    if message.channel.name == CHANNEL:
        for attachment in message.attachments:
            extension = attachment.filename[-4:]

            if extension.upper() not in [x.upper() for x in ALLOWED_FILES]:
                await message.channel.send("This file extension is not supported.")
                print("Bad File Extension: %s" % attachment.filename)
                continue

            url = attachment.url
            download_file(url)
            await message.channel.send("Upload successful.")


def download_file(url):
    extension = url[-4:]
    file = requests.get(url)
    unique_filename = str(uuid.uuid4())
    with open(IMG_DIR + "/" + unique_filename + extension, 'wb') as f:
        f.write(file.content)
    print("File Created: %s" % (unique_filename + extension))


client.run(TOKEN)
