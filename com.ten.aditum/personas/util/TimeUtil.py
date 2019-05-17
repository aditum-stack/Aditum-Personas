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
