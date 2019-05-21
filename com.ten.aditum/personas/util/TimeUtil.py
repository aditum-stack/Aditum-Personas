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


if __name__ == '__main__':
    time = "8:12:32"

    seconds = timeToS(time)
    print(seconds)

    newTime = sToTime(seconds)
    print(newTime)
