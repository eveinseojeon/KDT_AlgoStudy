from datetime import datetime
import math


def solution(fees, records):
    car = []
    car_num = []
    for i in records:
        t, c, io = i.split()
        car.append((datetime.strptime(t, "%H:%M"), c))
        car_num.append(c)

    car.sort(key=lambda x: (x[1], x[0]))
    car_num = list(set(car_num))
    car_num.sort()
    io_list = [[] for _ in range(len(car_num))]

    for n in car_num:
        for c in car:
            if n == c[1]:
                x = car_num.index(n)
                io_list[x].append(c)

    time_record = []
    for li in io_list:
        if len(li) % 2 != 0:
            li.append((datetime.strptime("23:59", "%H:%M"), li[0][1]))
        total_tr = 0
        for i in range(0, len(li), 2):
            tr = (li[i + 1][0] - li[i][0])
            tr = tr.seconds
            tr = tr // 60
            total_tr += tr
        time_record.append(total_tr)

    answer = []
    for j in time_record:
        if j <= fees[0]:
            answer.append(fees[1])
        else:
            an = fees[1] + math.ceil((j - fees[0]) / fees[2]) * fees[3]
            answer.append(an)

    return answer
