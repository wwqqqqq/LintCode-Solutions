class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count = 0
        x = 5
        while x <= n:
            count = count + int(n/x)
            x = x * 5
        return count

x = Solution()
print(Solution.trailingZeros(x,105))