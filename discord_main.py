import os
import discord
import logging
from discord.ext import commands
import army_date_calculate as army

TOKEN = os.environ["TOKEN"]

client = discord.Client()
bot = commands.Bot(command_prefix='-')
class MyClient(discord.Client):
    async def on_ready(self):
        print('{0}준비 완료!'.format(self.user))

    async def on_message(self, message):
        print("{0.author}에게서 온 DM : {0.content}".format(message))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('안녕'):
            await message.reply('안녕하세요!!', mention_author=True)

        if message.content.startswith('전역'):
            date = army.remain_days()
            date_percent = army.remain_days_percent()
            await message.reply("치비님의 남은 복무일 수는 " + date + "일이며 현재까지 " + date_percent + "%만큼 했습니다!")

logging.basicConfig(level=logging.INFO)
client = MyClient()
client.run(TOKEN)
