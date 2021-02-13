import discord
from discord.ext import commands
import logging

TOKEN = process.env.TOKEN

bot = commands.Bot(command_prefix='-')

class MyClient(discord.Client):
    async def on_ready(self):
        print('{0}준비 완료!'.format(self.user))

    async def on_message(self, message):
        print("{0.author}에게서 온 DM : {0.content}".format(message))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content == '안녕':
            await message.channel.send("안녕하세요!")

logging.basicConfig(level=logging.INFO)
client = MyClient()
client.run(TOKEN)
