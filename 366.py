"""
@param: n: an integer
@return: an ineger f(n)
"""
def fibonacci(n):
    i = 1
    a = 0
    b = 1
    while i < n:
        temp = a + b
        a = b
        b = temp
        i = i + 1
    return a

if __name__ == "__main__":
    n = int(input("n: "))
    print(fibonacci(n))