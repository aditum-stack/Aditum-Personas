import datetime


def timeToS(t):
    """
    时分秒转换成秒

    :param t: 时分秒
    :return: 秒
    """
    if t != '0':
        h, m, s = t.strip().split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        return 0


def sToTime(seconds):
    """
    秒转换成时分秒

    :param seconds: 秒
    :return: 时分秒
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def getTodayDate():
    """
    获取当天的日期信息

    :return: yyyy-MM-dd
    """
    # 日期前缀 20xx年
    date_prefix = "20"
    today = datetime.date.today()
    formatted_today = today.strftime('%y-%m-%d')
    return date_prefix + formatted_today


def getYesterdayDate():
    """
    获取昨天的日期信息

    :return: yyyy-MM-dd
    """
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


if __name__ == '__main__':
    # time = "8:12:32"

    # seconds = timeToS(time)
    # print(seconds)

    # newTime = sToTime(seconds)
    # print(newTime)

    today = getTodayDate()
    print(today)

    yesterday = getYesterdayDate()
    print(yesterday)
