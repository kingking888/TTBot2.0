
def make(e:str):
    r = []
    for index,item in enumerate(e):
        t = ord(item)
        if 0 <= t <= 127:
            r.append(t)
        if 128 <= t <= 2047:
            r.append(192 | 31 & t >> 6)
            r.append(128 | 63 & t)
        if 2048 <= t <= 55295 or 57344 <= t <= 65535:
            r.append(224 | 15 & t >> 12)
            r.append(128 | 63 & t >> 6)
            r.append(128 | 63 & t)
    for i in range(len(r)):
        r[i] &= 255
    return r

def encrypt(_string):
    n = []
    if not _string:
        return ""
    t = make(str(_string))
    for i in t:
        n.append(hex(5^i))
    return ''.join([x.replace('0x','') for x in n])
