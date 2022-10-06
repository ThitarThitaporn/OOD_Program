def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        if m > list[0]:
            return m
        else:
            return list[0]

input