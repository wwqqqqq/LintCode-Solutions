class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        if n < 1:
            return []
        front = self.fizzBuzz(n-1)
        if n % 3 == 0 and n % 5 == 0:
            front.append("fizz buzz")
        elif n % 3 == 0:
            front.append("fizz")
        elif n % 5 == 0:
            front.append("buzz")
        else:
            front.append(str(n))
        return front

x = Solution()
print(Solution.fizzBuzz(x, 15))