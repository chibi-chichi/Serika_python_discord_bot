import os
import random
import discord
import logging
import traceback
import army_date_calculate as army
import spread_sheet_reader as excel
import bang_dream_score_caluclator as bangdream


TOKEN = os.environ["TOKEN"]

client = discord.Client()

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
    
    # 인사를 건냅니다.
        if message.content.startswith('-안녕'):
            await message.reply('안녕하세요!!', mention_author=True)
    
    # 제작자의 남은 군생활을 알려줍니다.    
        if message.content.startswith('-복무일'):
            date = army.remain_days()
            date_percent = army.remain_days_percent()
            await message.channel.send("치비님의 남은 전역일 수는 " + date + "일이며 현재까지 " + date_percent + "%만큼 했어요!")
    
    # 로또 번호를 뽑아줍니다. 낙첨되도 책임은 지지 않습니다...  
        if message.content.startswith('-로또'):
            # 로또 번호 1~45까지의 숫자를 뽑아줍니다.
            possible_number_list = random.sample(range(1,45), 6)
            # 로또 번호를 보기 편하게 숫자 크기 순으로 정렬해줍니다.
            possible_number_list = sorted(possible_number_list)
            # 로또 번호를 출력하기 위해 문자열로 바꾸고 출력하기 편하게 바꿔줍니다.
            number_list = ", ".join([str(numb) for numb in possible_number_list])
            await message.channel.send("이번 로또 추첨번호는 `" + number_list + "` 가 좋을 것 같아요!")
    
    # 0~10 중에서의 숫자를 뽑아줍니다. 
        if message.content.startswith('-추첨'):
            # 디스코드 이모지인 숫자들의 리스트
            possible_numb = [":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:"]
            # 숫자들의 리스트에서 하나를 뽑아줍니다.
            picked = random.choice(possible_numb)
            await message.channel.send("숫자 " + picked + "가 나왔어요!")

        if message.content.startswith('-전적'):
            nickname = message.content[4:]
            nickname = nickname.replace(" ", "%20")
            opggwebsite = 'https://www.op.gg/summoner/userName='
            await message.channel.send(opggwebsite + nickname)
    
    # 선택장애를 위해 선택을 대신 해줍니다.
        if message.content.startswith('-선택'):
            # 메세지를 불러옵니다
            choice_msg = message.content
            # .split()을 위해 "-선택" 이라는 단어를 제거합니다.
            wanted_choice = choice_msg[3:]
            # 선택지를 나눠 리스트화시킵니다.
            select_choose = wanted_choice.split()
            # 리스트화 된 선택지에서 하나를 골라줍니다.
            choose = random.choice(select_choose)
            await message.channel.send(choose + "(이)가 좋을 것 같아요!")

    # 구글 스프레드시트에 저장해둔 리듬게임의 최고 기록들을 가져옵니다. 개인적으로 사용하는 기능입니다.
        if message.content.startswith('-엑셀'):
            try:
                # 구글 스프레드시트에서 스프레드시트 파일을 가져옵니다.
                excel.sync_spread()
                # 메세지를 보내는 사람이 원하는 게임 이름과 곡을 가져옵니다. 이 때 곡은 제목을 치기엔 공식적으로 규정된 한국어 번역이 없기에 숫자로 대체합니다.
                get_game_title = message.content.split()
                # 찾고자 하는 리듬 게임 제목을 불러옵니다.
                gametitle = get_game_title[1]
                # 찾고자 하는 리듬 게임 곡을 불러옵니다.
                gamesong = get_game_title[2]
                
                # 저장해둔 리듬게임과 그 게임 내부의 곡을 가져오는 역활을 합니다.
                imform = excel.spread_information(gametitle, gamesong)
                # embed로 메세지 출력합니다.
                await message.reply(embed=imform)

            except Exception as e:
                # 문제가 있으면 디스코드 채팅에 로그를 출력합니다. 만약 에러가 나온다면 꼭 알려주세요.
                await message.reply("문제가 발생했어요!")
                await message.reply(traceback.format_exc())
                
    # 뱅드림! 걸즈 밴드 파티의 예상 스코어 계산기입니다.
        if message.content.startswith('-방도리'):
            try:
                # 유저의 정보를 가져옵니다. 각각 곡의 난이도, 노트 개수, 밴드 종합력.
                get_information = message.content.split()
                song_difficulty = int(get_information[1])
                song_notes = int(get_information[2])
                total_power = int(get_information[3])
                # 노트당 스코어를 가져옵니다.
                notes_score = bangdream.note_score_calculate(song_difficulty, song_notes, total_power)
                # 전체 곡의 스코어를 예상해서 가져옵니다.
                total_score = bangdream.total_score_calculate(notes_score, song_notes)
                await message.reply("제 생각 그 곡에서는 " + str(total_score) + " 정도 나올 것 같아요!")

            except IndexError as e:
                # 너무 높은 숫자를 주거나 무언가가 틀리면 에러 메세지가 나옵니다.
                await message.reply("무언가가 잘 못 주신 것 같아요! -방도리 [난이도] [노트 갯수] [종합력]순으로 넣어주세요!")

            except TypeError as e:
                # 정수가 아닌 문자열을 주면 에러 메세지가 나옵니다. 추가로 에러 로그까지 같이 나옵니다.
                await message.reply("글자말고 숫자를 넣어주세요!")
                await message.reply(traceback.format_exc())
                
    # 디스코드 내에서 사용할 수 있는 기능을 소개해줍니다.
        if message.content.startswith('-설명'):
            await message.channel.send("안녕하세요! 치비님의 인공비서 하코자키 세리카에요! \n\n현재 사용할 수 있는 기능으로는\n```fix\n-복무일 : 개발자의 남은 복무일수를 알려주는 기능이예요!.\n"
                                       "-로또 : 로또 번호를 6개 선택해드려요! 로또 번호를 추첨해서 뽑으면 뽑힐 때 기분이 더 좋아지는 효과가 있다고 해요!\n"
                                       "-추첨 : 마음에 드는 숫자 0 에서 10까지 무작위로 골라드려요!.\n"
                                       "-선택 [선택지1, 선택지2, ...] : 선택을 쉽게 못하는 여러분을 위해 제가 선택해요! 그런데 저는 선택지에서 좋은 것을 고르고 있는걸까요...?"
                                       "-엑셀 [게임 이름] [엑셀 열 번호] : 개발자의 여러가지 직업(?)에서 각 곡에서 제일 좋았던 기록을 알려주어요! 아직 엑셀은 완성이 되지 않아서 비어있는 곡들이 많을거에요!"
                                       "-방도리 [곡 난이도] [노트 개수] [밴드 종합력(에어리어 아이템 포함)] : 뱅드림이라는 게임에서 나오는 점수를 대충이나마 예상을 해주어요! 이 개발자는 이런 곳에서 있어도 괜찮은걸까요?```\n가 있어요!")
#기본적인 정보들을 로그에 출력해줍니다.
logging.basicConfig(level=logging.INFO)

client = MyClient()
client.run(TOKEN)
