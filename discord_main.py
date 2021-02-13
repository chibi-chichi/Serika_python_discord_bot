import discord
from discord.ext import commands
import logging
import army_date_calculate as army
TOKEN = process.env.TOKEN

bot = commands.Bot(command_prefix='-')
class MyClient(discord.Client):
    async def on_ready(self):
        print('{0}준비 완료!'.format(self.user))

    async def on_message(self, message):
        print("{0.author}에게서 온 DM : {0.content}".format(message))

@bot.command(pass_context=True)
async def on_message(ctx):
    if ctx.content == '안녕':
        await ctx.channel.send("안녕하세요!")

@bot.command(pass_context=True)
async def army_date(ctx):
    if ctx.content == '전역일':
        print(army.remain_days())
        print(army.remain_days_percent())
        await ctx.channel.send("치비님의 남은 전역일 수는" + army.remain_days() + "일이며 현재" + army.remain_days_percent() + "%만큼 했습니다!")

logging.basicConfig(level=logging.INFO)
client = MyClient()
client.run(TOKEN)
