import collections


# 입력 1
n1 = 5
arr11 = [9, 20, 28, 18, 11]
arr12 = [30, 1, 21, 17, 28]

# 출력 1
output1 = ["#####", "# # #", "### #", "#  ##", "#####"]


# 입력 2
n2 = 6
arr21 = [46, 33, 33, 22, 31, 50]
arr22 = [27, 56, 19, 14, 14, 10]

# 출력 2
output2 = ["######", "###  #", "##  ##", " #### ", " #####", "### # "]


def solution(n, arr1, arr2):
    maps = []
    for i in range(n):
        maps.append(
            bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace('1', '#')
                .replace('0', ' ')
        )
    return maps


print(solution(n1, arr11, arr12))
print(solution(n1, arr11, arr12) == output1)
print(solution(n2, arr21, arr22))
print(solution(n2, arr21, arr22) == output2)


# --------------------------------------------------
# 입력
n1 = "1S2D*3T"
n2 = "1D2S#10S"
n3 = "1D2S0T"
n4 = "1S*2T*3S"
n5 = "1D#2S*3S"
n6 = "1T2D3D#"
n7 = "1D2S3T*"

# 출력
a1 = 37
a2 = 9
a3 = 3
a4 = 23
a5 = 5
a6 = -4
a7 = 59


def solution1(dartResult):
    nums = [0]
    
    for s in dartResult:
        if s == "S":
            nums[-1] **= 1
            nums.append(0)
        elif s == 'D':
            nums[-1] **= 2
            nums.append(0)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
        elif s == '*':
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2
        elif s == '#':
            nums[-2] *= -1
        else:
            nums[-1] = nums[-1] * 10 + int(s)
    
    return sum(nums)


print(solution1(n1))
print(solution1(n1) == a1)
print(solution1(n2))
print(solution1(n2) == a2)
print(solution1(n3))
print(solution1(n3) == a3)
print(solution1(n4))
print(solution1(n4) == a4)
print(solution1(n5))
print(solution1(n5) == a5)
print(solution1(n6))
print(solution1(n6) == a6)
print(solution1(n7))
print(solution1(n7) == a7)


# --------------------------------------------------
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


def solution2(cacheSize, cities):
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


print(solution2(s1, c1))
print(solution2(s1, c1) == a1)
print(solution2(s2, c2))
print(solution2(s2, c2) == a2)
print(solution2(s3, c3))
print(solution2(s3, c3) == a3)
print(solution2(s4, c4))
print(solution2(s4, c4) == a4)
print(solution2(s5, c5))
print(solution2(s5, c5) == a5)
print(solution2(s6, c6))
print(solution2(s6, c6) == a6)
