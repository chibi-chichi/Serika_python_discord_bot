import math

def theater_point_calculation(current_score, object_score, items):
    MM_live = 0
    M6_ticket = 0
    M6_live = 0
    M4_ticket = 0
    M4_live = 0
    M2plus_ticket = 0
    M2plus_live = 0
    M2_ticket = 0
    M2_live = 0
    needed_point = 600
    MM_ticket_maximum_play = math.fabs(needed_point / 59.5)
    #needed_point = object_score - current_score
    # 얻는 포인트와 재화의 갯수는 같음 ?
    # 여기서 59.5는 MM 티켓 1회 pt
    # needed_point = (getting_item_point / 180 * 537) + getting_item_point
    # 순서대로 MM 티켓 / 라이브, 6M 티켓 / 라이브, 4M 티켓 / 라이브, 2M+ 티켓 / 라이브, 2M 티켓 / 라이브
    # 각 플레이 난이도별로 올림수를 해야하기때문에 ceil 도배
    getting_item = math.ceil(59.5 * MM_ticket_maximum_play) + math.ceil(85.0 * a) + math.ceil(45.0 * b) + math.ceil(64.0 * c) + math.ceil(34.3 * d) + math.ceil(49.0 * e) + math.ceil(43.4 * f) + math.ceil(62.0 * g) + math.ceil(25.0 * h) + math.ceil(35.0 * i)
    getting_point = ((getting_item / 180) * 537) + getting_item
    while needed_point < getting_point:
        MM_ticket_maximum_play = MM_ticket_maximum_play - 1
        for a in range(20):
            MM_live = MM_live + 1
            if MM_live == 20:
                MM_live = 0
                for b in range(20):
                    M6_ticket = M6_ticket + 1
                    if M6_ticket == 20:
                        M6_ticket = 0
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


def tour_point_calculation(current_score, object_score, items, progressivity):
    #공식이 진짜 뭐였지
    print("투어")

if __name__ == '__main__':
    main()
