lst = [3,43,7,456,435,6,7,435,5,6,2,34,21,4]

# --------------------------------------------------
def bubblesort(A):
    for i in range(1, len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


print(bubblesort(lst[:]))


# --------------------------------------------------
def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)
    


quicksort(lst, 0, len(lst)-1)
lst