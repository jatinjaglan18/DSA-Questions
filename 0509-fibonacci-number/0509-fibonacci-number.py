def fibo(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    res = fibo(i-1) + fibo(i-2)
    return res
class Solution:
    def fib(self, n: int) -> int:
        return fibo(n)