import math

def theater_point_calculation(current_score, object_score, items):
    current_score = int(current_score)
    object_score = int(object_score)
    items = int(items)
    needed_point = object_score - (current_score + (math.fabs(items / 180) * 537))
    #MM_ticket_maximum_play = math.fabs(needed_point / 59.5)
    #needed_point = object_score - current_score
    # 얻는 포인트와 재화의 갯수는 같음 ?
    # 여기서 59.5는 MM 티켓 1회 pt
    # needed_point = (getting_item_point / 180 * 537) + getting_item_point
    # 순서대로 MM 티켓 / 라이브, 6M 티켓 / 라이브, 4M 티켓 / 라이브, 2M+ 티켓 / 라이브, 2M 티켓 / 라이브
    # 각 플레이 난이도별로 올림수를 해야하기때문에 ceil 도배
    getting_point = needed_point #((getting_item / 180) * 537) + getting_item
    while needed_point > getting_point:
        global MM_ticket
        global MM_live
        global M6_ticket
        global M6_live
        global M4_ticket
        global M4_live
        global M2plus_ticket
        global M2plus_live
        global M2_ticket
        global M2_live
        getting_item = 0
        MM_ticket = 0
        MM_live = 0
        M6_ticket = 0
        M6_live = 0
        M4_ticket = 0
        M4_live = 0
        M2plus_ticket = 0
        M2plus_live = 0
        M2_ticket = 0
        M2_live = 0
        for m2live in range(20):
            if getting_item == needed_point:
                answer = [MM_ticket, MM_live, M6_ticket, M6_live, M4_ticket, M4_live, M2plus_ticket, M2plus_live, M2_ticket, M2_live]
                print(MM_ticket, MM_live, M6_ticket, M6_live, M4_ticket, M4_live, M2plus_ticket, M2plus_live, M2_ticket, M2_live)
                return answer
                break
            M2_live = M2_live + 1
            for m2ticket in range(20):
                if getting_item == needed_point:
                    break
                M2_ticket = M2_ticket + 1
                for m2plive in range(20):
                    if getting_item == needed_point:
                        break
                    M2plus_live = M2plus_live + 1
                    for m2pticket in range(20):
                        if getting_item == needed_point:
                            break
                        M2plus_ticket = M2plus_ticket + 1
                        for m4live in range(20):
                            if getting_item == needed_point:
                                break
                            M4_live = M4_live + 1
                            for m4ticket in range(20):
                                if getting_item == needed_point:
                                    break
                                M4_ticket = M4_ticket + 1
                                for m6live in range(20):
                                    if getting_item == needed_point:
                                        break
                                    M6_live = M6_live + 1
                                    for m6ticket in range(20):
                                        if getting_item == needed_point:
                                            break
                                        M6_ticket = M6_ticket + 1
                                        for mmlive in range(20):
                                            if getting_item == needed_point:
                                                break
                                            MM_live = MM_live + 1
                                            for mmticket in range(20):
                                                if getting_item == needed_point:
                                                    break
                                                MM_ticket = MM_ticket + 1
                                                getting_item = (math.ceil(59.5 * MM_ticket) + math.ceil(85.0 * MM_live) + math.ceil(
                                                    45.0 * M6_ticket) + math.ceil(64.0 * M6_live) + math.ceil(34.3 * M4_ticket) + math.ceil(
                                                    49.0 * M4_live) + math.ceil(43.4 * M2plus_ticket) + math.ceil(62.0 * M2plus_live) + math.ceil(
                                                    25.0 * M2_ticket) + math.ceil(35.0 * M2_live) / 180 * 537 + getting_item)

        if needed_point == getting_point:
            print("성공!")
            break
        '''
        for MM_ticket in range(maximum_play):
            MM_ticket_playcount = maximum_play
            MM_ticket_point = MM_ticket_playcount * 59.5
            if MM_ticket_point == needed_point:
                print(MM_ticket_playcount)
                break
            elif MM_ticket_point <= needed_point:
                MM_ticket_playcount = MM_ticket_playcount - 1
            elif MM_ticket_playcount < 0:
        '''
    answer = [MM_ticket, MM_live, M6_ticket, M6_live, M4_ticket, M4_live, M2plus_ticket, M2plus_live, M2_ticket,
              M2_live]
    return answer

def tour_point_calculation(current_score, object_score, items, progressivity):
    #공식이 진짜 뭐였지
    print("투어")

if __name__ == '__main__':
    main()

    
        # 아이돌마스터 밀리언 라이브 시어터 데이즈 투어 이벤트와 시어터 이벤트의 점수아트 계산기입니다. 아직 미완성입니다.
 #'''       if message.content.startswith('-투어') or message.content.startswith('-시어터'):
 #           try:
 #               get_message = message.content.split()
 #               # 투어 이벤트 점수아트 계산기
 #               if get_message[0] == "-투어":
 #                   MLTH.tour_point_calculation(get_message[1], get_message[2], get_message[3], get_message[4])
 #                   await message.reply("이게 뭐예요?")
 #               # 시어터 이벤트 점수아트 계산기
 #               elif get_message[0] == "-시어터":
 #                   MLTH.theater_point_calculation(get_message[1], get_message[2], get_message[3])
 #                   await message.reply("히이이이익")
       # 에러가 생기면 에러 로그가 나옵니다. 아직 미완성입니다.
 #           except Exception as e:
 #               await message.reply(traceback.format_exc())
 #               '''
