from datetime import timedelta, date
import datetime
import time

def remain_days():
    today = date.today() #현재 시간을 가져옴 (YYYY-MM-DD)
    dead_end = datetime.date(2022, 2, 2) #전역일 (YYYY-MM-DD)

    object = abs(today - dead_end) #남은 일수를 알려줌 (DDD Days)
    object_days = object.days #남은 일자를 숫자로만 출력시킴
    object_day = str(object_days)
    return object_day

def remain_days_percent():
    object_days = int(remain_days())
    object_days_percent = round(abs((object_days - 548) / 548 * 100), 2)
    object_days_percent = str(object_days_percent)
    return object_days_percent

if __name__ == '__main__':
    main()
