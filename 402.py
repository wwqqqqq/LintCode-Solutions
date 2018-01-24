
"""
@param: A: An integer array
@return: A list of integers includes the index of the first number and the index of the last number
"""
def FindMaxArray(A, st, ed):
    if st==ed:
        return (A[st], st, ed)
    if st>ed:
        return (-1000, st, ed)
    mid = int((st + ed)/2)
    # print("call", (st, mid-1), (mid+1,ed))
    (left, st1, ed1) = FindMaxArray(A, st, mid-1)
    (right, st2, ed2) = FindMaxArray(A, mid+1, ed)
    # print("return", (st, ed))
    if left<right:
        res = (right, st2, ed2)
    else:
        res = (left, st1, ed1)
    right = 0
    left = 0
    i = mid + 1
    ed3 = mid
    s = 0
    while i <= ed:
        s = s + A[i]
        if s > right:
            right = s
            ed3 = i
        i = i + 1
    i = mid - 1
    st3 = mid
    s = 0
    while i >= st:
        s = s + A[i]
        if s > left:
            left = s
            st3 = i
        i = i - 1
    s = right + left + A[mid]
    if res[0]<s:
        res = (s, st3, ed3)
    # print((st, ed),"res",res)
    return res
        
def continuousSubarraySum(A):
    length = len(A)
    res = FindMaxArray(A, 0, length-1)
    print([res[1],res[2]])

if __name__ == "__main__":
    A = [-3, 1, 3, -3, 4]
    continuousSubarraySum(A)