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


def solution(dartResult):
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


print(solution(n1))
print(solution(n1) == a1)
print(solution(n2))
print(solution(n2) == a2)
print(solution(n3))
print(solution(n3) == a3)
print(solution(n4))
print(solution(n4) == a4)
print(solution(n5))
print(solution(n5) == a5)
print(solution(n6))
print(solution(n6) == a6)
print(solution(n7))
print(solution(n7) == a7)
