import os
import discord
import logging
from discord.ext import commands
import army_date_calculate as army
import lotto_number as lotto

TOKEN = os.environ["TOKEN"]

client = discord.Client()
bot = commands.Bot(command_prefix='-')
class MyClient(discord.Client):
    async def on_ready(self):
        #건설로봇 준비완료
        print('{0}준비 완료!'.format(self.user))

    async def on_message(self, message):
        #DM에서 무슨 메세지를 보냈는데 log로 확인합니다.
        print("{0.author}에게서 온 DM : {0.content}".format(message))

    async def on_message(self, message):
        #메세지를 보낸 유저가 봇이 아닌 유저인지 확인해줍니다.
        if message.author.id == self.user.id:
            return
    
    #인사를 건냅니다.
        if message.content.startswith('-안녕'):
            await message.reply('안녕하세요!!', mention_author=True)
    
    #진짜 수정한거 맞는 지 확인합니다. 고쳐졌다면서 안고쳐져있지만        
        if message.content.startswith('-수정'):
            await message.reply('고쳐졌어요!!', mention_author=True)
    
    #제작자의 남은 군생활을 알려줍니다.    
        if message.content.startswith('-복무일'):
            date = army.remain_days()
            date_percent = army.remain_days_percent()
            await message.channel.send("치비님의 남은 전역일 수는 " + date + "일이며 현재까지 " + date_percent + "%만큼 했습니다!")
      
        if message.content.startswith('-로또'):
            number_list = lotto.lotto_number_list()
            bonus_number = lotto.bonus_number()
            await message.channel.send("이번 로또 추첨번호는" + number_list + "그리고 보너스 숫자는" + bonus_number + "가 좋을 것 같아요!")


#기본적인 정보들을 로그에 출력해줍니다.
logging.basicConfig(level=logging.INFO)

client = MyClient()
client.run(TOKEN)
