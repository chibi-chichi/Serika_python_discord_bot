import urllib
import json
import discord

'''
event_url = "https://api.matsurihi.me/mltd/v1/events/"
request_url = urllib.request.Request(event_url)
response_url = urllib.request.urlopen(request_url)
event_data = response_url.read()
encoded = event_data.decode(encoding='UTF-8')
convert_todict = eval(encoded)

#이벤트 넘버 불러오기 해야함

event_number = str(70)
rankingborder = "/ranking/borderPoints"
'''
#eventRankingUrl = event_url + event_number + rankingborder
#print(eventRankingUrl)

eventRankingUrl = "https://api.matsurihi.me/mltd/v1/events/194/rankings/borderPoints"
request = urllib.request.Request(eventRankingUrl)
response = urllib.request.urlopen(request)
data = response.read()
encoded = data.decode(encoding='UTF-8')
convertdict = eval(encoded)

def get_values():
    values = list(convertdict.values())
    get_border = values[0]["scores"]
    return get_border

def get_keys():
    keys = list(convertdict.keys())
    keys = keys[0]
    return keys

def get_embed():
    values = list(convertdict.values())
    values = values[0]
    call_values = get_values()
    summary_time = values["summaryTime"].replace("T", "\n")
    borderEmbed = discord.Embed(title="**밀리시타 이벤트 보더**", description=summary_time, color=0x9B59B6)
    borderEmbed.add_field(name="MLTD Event Point Border", value='Platinum Star Theater', inline=False)
    borderEmbed.add_field(name=call_values[0]["rank"], value=int(call_values[0]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[1]["rank"], value=int(call_values[1]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[2]["rank"], value=int(call_values[2]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[3]["rank"], value=int(call_values[3]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[4]["rank"], value=int(call_values[4]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[5]["rank"], value=int(call_values[5]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[6]["rank"], value=int(call_values[6]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[7]["rank"], value=int(call_values[7]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[8]["rank"], value=int(call_values[8]["score"]), inline=True)
    borderEmbed.add_field(name=call_values[9]["rank"], value=int(call_values[9]["score"]), inline=True)
    return borderEmbed