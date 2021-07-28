import os
from json.tool import main

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import traceback
import discord


# 구글 스프레드시트를 가져옵니다.
def sync_spread():
    try:
        scopes = ['https://spreadsheets.google.com/feeds',
                  'https://www.googleapis.com/auth/drive']
        json_creds = os.getenv("GOOGLE_KEYS")
        creds_dict = json.loads(json_creds)
        creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
        gc = gspread.authorize(creds)
        return gc

    # 문제가 생기면 에러 로그를 출력합니다.
    except Exception as e:
        print(traceback.format_exc())


def spread_information(game_title, game_song):
    google_spread = sync_spread()  # 구글 스프레드시트와 공유해서 출력하게 해줍니다.
    gc1 = google_spread.open("리듬게임 스코어링 시트").worksheet(game_title)  # 각 게임의 엑셀을 찾아가줍니다.
    title = gc1.row_values(1)  # 엑셀의 정렬한 순서를 나타냅니다.
    game_song = int(game_song) + 1  # 1은 title이 출력이 되기 때문에 1부터 시작할려면 +1을 해줘야합니다.
    # score_values = gc1.row_values(game_song)
    # japan_name = score_values[1]
    # 위에 있는 코드들은 엑셀이 다 채워진 후 최적화를 해줄겁니다.

    # 엄청난 노가다의 빛으로 비어있는 엑셀칸까지 다 출력해줍니다.
    japan_name = str(gc1.acell('B' + str(game_song)).value)
    korean_name = str(gc1.acell('C' + str(game_song)).value)
    song_type = str(gc1.acell('D' + str(game_song)).value)
    artist = str(gc1.acell('E' + str(game_song)).value)
    difficulty = str(gc1.acell('F' + str(game_song)).value)
    perfect_note = str(gc1.acell('G' + str(game_song)).value)
    great_note = str(gc1.acell('H' + str(game_song)).value)
    good_note = str(gc1.acell('I' + str(game_song)).value)
    badfastslow_note = str(gc1.acell('J' + str(game_song)).value)
    miss_note = str(gc1.acell('K' + str(game_song)).value)
    total_note = str(gc1.acell('L' + str(game_song)).value)
    max_combo = str(gc1.acell('M' + str(game_song)).value)
    full_combo = str(gc1.acell('N' + str(game_song)).value)
    best_score = str(gc1.acell('O' + str(game_song)).value)

    # 노래 제목을 한 번에 출력시켜주는 변수를 생성했습니다.
    song_title = japan_name + "\t" + korean_name

    # 만약 제목이 일본어와 한국어가 같은 영어일 시에 노래 제목은 하나만 출력하도록 합니다.
    if japan_name == korean_name:
        song_title = japan_name
    # 디스코드에서 출력되는 메세지를 embed로 정리했습니다. embed에 추후 앨범 커버 사진 추가 예정
    embed = discord.Embed(title="베스트 스코어", description='자신이 가장 플레이 한 곡 중에서 제일 잘한 기록을 가져옵니다.', color=0x9B59B6)
    embed.add_field(name="__TITLE__", value=song_title, inline=True)
    embed.add_field(name="__" + title[3] + "__", value=song_type, inline=True)
    embed.add_field(name="__" + title[4] + "__", value=artist, inline=False)
    embed.add_field(name="__" + title[5] + "__", value=difficulty, inline=False)
    # embed.add_field(name="__ADJUSTMENT__",
    #                value="**" + title[6] + "**\t" + perfect_note + "\n**" + title[7] + "**\t" + great_note + "\n**" +
    #                      title[8] + "**\t" + good_note + "\n**" + title[9] + "**\t" + badfastslow_note + "\n**" +
    #                      title[10] + "**\t" + miss_note + "\n**" + title[11] + "**\t" + total_note + "\n**" + title[
    #                          12] + "**\t" + max_combo + "\n**" + title[13] + "**\t" + full_combo, inline=False)
    embed.add_field(name=title[6], value=perfect_note, inline=True)
    embed.add_field(name=title[7], value=great_note, inline=True)
    embed.add_field(name=title[8], value=good_note, inline=True)
    embed.add_field(name=title[9], value=badfastslow_note, inline=True)
    embed.add_field(name=title[10], value=miss_note, inline=True)
    embed.add_field(name=title[11], value=total_note, inline=True)
    embed.add_field(name=title[12], value=max_combo, inline=True)
    embed.add_field(name=title[13], value=full_combo, inline=True)
    embed.add_field(name="__HIGH SCORE__", value=best_score, inline=False)
    return embed


if __name__ == '__main__':
    main()
