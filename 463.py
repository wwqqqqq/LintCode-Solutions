def sortIntegers(A):
    i = 0
    length = len(A)
    while i < length - 1:
        j = length - 1
        while j > i:
            if A[j]<A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
            j = j - 1
        i = i + 1
    return A

A = [3, 1, 2, 5, 4]
print(sortIntegers(A))