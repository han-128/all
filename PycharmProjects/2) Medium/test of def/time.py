def read(seconds):
    h = seconds // 3600
    m = seconds // 60 % 60
    s = seconds % 60

    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    if s < 10:
        s = "0" + str(s)

    print(f"{h}:{m}:{s}")


read(3685)