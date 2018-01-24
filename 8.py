class Solution:
    """
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        if len(str) == 0:
            return
        elif offset > len(str):
            offset = offset % len(str)
        elif offset == len(str):
            return
        length = len(str)-offset
        str1 = str[:length]
        str2 = str[length:]
        str[:offset] = str2
        str[offset:] = str1


x = Solution()
Solution.rotateString(x, "abcdefg", 3)