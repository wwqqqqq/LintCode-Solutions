
def mergeSortedArray(A, B):
    lenA = len(A)
    lenB = len(B)
    C = []
    i, j, k = 0, 0, 0
    while i < lenA and j < lenB:
        if A[i] <= B[j]:
            C.append(A[i])
            k = k + 1
            i = i + 1
        else:
            C.append(B[j])
            j = j + 1
            k = k + 1
    if i == lenA:
        C = C + B[j:]
    else:
        C = C + A[i:]
    return C

A = [1, 2, 3, 4]
B = [2, 4, 5, 6]
print(mergeSortedArray(A,B))