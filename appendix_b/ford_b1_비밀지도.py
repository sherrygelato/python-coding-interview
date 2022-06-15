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
