def solution(a, b):
    today=0
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        today+=month[i]
    return day[(today+b)%7]
