import collections


# 입력
s1 = 3
c1 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
s2 = 3
c2 = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
s3 = 2
c3 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
s4 = 5
c4 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
s5 = 2
c5 = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
s6 = 0
c6 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

# 출력
a1 = 50
a2 = 21
a3 = 60
a4 = 52
a5 = 16
a6 = 25


def solution(cacheSize, cities):
    elapsed = 0
    cache = collections.deque(maxlen = cacheSize)
    
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            elapsed += 1
        else:
            cache.append(c)
            elapsed += 5
    return elapsed


print(solution(s1, c1))
print(solution(s1, c1) == a1)
print(solution(s2, c2))
print(solution(s2, c2) == a2)
print(solution(s3, c3))
print(solution(s3, c3) == a3)
print(solution(s4, c4))
print(solution(s4, c4) == a4)
print(solution(s5, c5))
print(solution(s5, c5) == a5)
print(solution(s6, c6))
print(solution(s6, c6) == a6)
