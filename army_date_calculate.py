from datetime import timedelta, date
import datetime
import time

    # 남은 군생활 일수를 알려줍니다.
def remain_days():
    today = date.today()                    # 현재 시간을 가져옵니다. (YYYY-MM-DD)
    dead_end = datetime.date(2022, 2, 2)    # 축 전역일 (YYYY-MM-DD)


    object = abs(today - dead_end)          # 남은 일수를 알려줍니다. (DDD Days)
    object_days = object.days               # 남은 일자를 숫자로만 출력시켜줍니다.
    object_day = str(object_days)
    return object_day
    
    # 남은 군 생활을 퍼센테이지로 나타내줍니다.
def remain_days_percent():
    object_days = int(remain_days())
    object_days_percent = round(abs((object_days - 548) / 548 * 100), 2)    # 남은 일수의 퍼센테이지를 구합니다. 그 날이 올까?
    object_days_percent = str(object_days_percent)
    return object_days_percent

if __name__ == '__main__':
    main()
