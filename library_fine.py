def fine(returned, due):
    d1, m1, y1 = map(int, returned.split())
    d2, m2, y2 = map(int, due.split())
    if y2 < y1:
        return 10000
    elif y2 > y1:
        return 0
    if m2 < m1:
        return (m1 - m2) * 500
    elif m2 > m1:
        return 0
    if d2 < d1:
        return (d1 - d2) * 15
    elif d2 > d1:
        return 0
    return 0
print(fine(input().strip(), input().strip()))   