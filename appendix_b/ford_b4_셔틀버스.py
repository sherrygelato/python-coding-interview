import collections


# 입력
n1 = 1
t1 = 1
m1 = 5
timetable1 = ["08:00", "08:01", "08:02", "08:03"]
n2 = 2
t2 = 10
m2 = 2
timetable2 = ["09:10", "09:09", "08:00"]
n3 = 2
t3 = 1
m3 = 2
timetable3 = ["09:00", "09:00", "09:00", "09:00"]
n4 = 1
t4 = 1
m4 = 5
timetable4 = ["00:01", "00:01", "00:01", "00:01", "00:01"]
n5 = 1
t5 = 1
m5 = 1
timetable5 = ["23:59"]
n6 = 10
t6 = 60
m6 = 45
timetable6 = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

# 출력
a1 = "09:00"
a2 = "09:09"
a3 = "08:59"
a4 = "00:00"
a5 = "09:00"
a6 = "18:00"


def solution(n, t, m, timetable):
    timetable = [
        int(time[:2])*60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()
    
    current = 540
    
    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) - 1
            else:
                candidate = current
        
        current += t
    
    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)


print(solution(n1, t1, m1, timetable1))
print(solution(n1, t1, m1, timetable1) == a1)
print(solution(n2, t2, m2, timetable2))
print(solution(n2, t2, m2, timetable2) == a2)
print(solution(n3, t3, m3, timetable3))
print(solution(n3, t3, m3, timetable3) == a3)
print(solution(n4, t4, m4, timetable4))
print(solution(n4, t4, m4, timetable4) == a4)
print(solution(n5, t5, m5, timetable5))
print(solution(n5, t5, m5, timetable5) == a5)
print(solution(n6, t6, m6, timetable6))
print(solution(n6, t6, m6, timetable6) == a6)
