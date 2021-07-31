import discord
import json
import urllib.request


# 최신의 이벤트 정보를 얻습니다.
def get_event_info():
    event_url = "https://api.matsurihi.me/mltd/v1/events/"
    request_url = urllib.request.Request(event_url)
    response_url = urllib.request.urlopen(request_url)
    event_data = response_url.read()
    encoded = event_data.decode(encoding='UTF-8')
    convert_todict = json.loads(encoded)
    event_id = list(convert_todict[-1].values())
    return event_id


# 이벤트 보더를 얻습니다.
def get_border():
    event_id = get_event_info()
    eventRankingUrl = "https://api.matsurihi.me/mltd/v1/events/" + str(event_id[0]) + "/rankings/borderPoints"
    # eventRankingUrl = "https://api.matsurihi.me/mltd/v1/events/" + "194" + "/rankings/borderPoints"
    request = urllib.request.Request(eventRankingUrl)
    response = urllib.request.urlopen(request)
    data = response.read()
    encoded = data.decode(encoding='UTF-8')
    convertdict = json.loads(encoded)
    return convertdict


# 최신 이벤트의 타입을 얻습니다.
def get_event_type():
    event_type_dict = {'0': 'Showtime', '1': 'Millicolle', '2': 'Theater', '3': 'Tour', '4': 'Anniversary'
        , '5': 'Twinstage', '6': 'Tune', '7': 'tale', '8': 'pst'}
    event_type = get_event_info()
    return event_type_dict.get(str(event_type[2]))


def get_values(convertdict):
    values = list(convertdict.values())
    border = values[0]["scores"]
    return border


def get_keys(convertdict):
    keys = list(convertdict.keys())
    keys = keys[0]
    return keys


def get_embed():
    try:
        convertdict = get_border()
        values = list(convertdict.values())
        values = values[0]
        call_values = get_values(convertdict)
        summary_time = values["summaryTime"].replace("T", "\n")
        borderEmbed = discord.Embed(title="**밀리시타 이벤트 보더**", description=summary_time, color=0x9B59B6)
        borderEmbed.add_field(name="MLTD Event Point Border", value='Platinum Star Theater', inline=False)
        for value in call_values:
            try:
                if value["score"] is None:
                    value["score"] = "0"
                borderEmbed.add_field(name=value["rank"], value=int(value["score"]), inline=True)
            except TypeError:
                pass
        borderEmbed.add_field(name="업데이트 주기 변경", value="30분\0 1시간\0 12시간\0 24시간")
        return borderEmbed
    except AttributeError:
        return -1
