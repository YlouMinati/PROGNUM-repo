#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""

    def nth(self, N):
        a, b = 0, 1

        for _ in range(N - 1):
            a, b = b, a + b

        return a

    def div(self, N, M):
        a, b = 0, 1
        res = []

        for _ in range(N):
            if a % M == 0:
                res.append(a)

            a, b = b, a + b

        return res


fib = Fibonacci()



# test
# print(fib.nth(100))
# print(fib.div(100, 7))

N= int(input('the N-th term of the fibonacci sequence: ...'))
M= int(input('that can be divided by : ...'))

print(f'the N-th term of the fibonacci sequence is : {fib.nth(N)}')
print(f'all Fibonacci numbers less than N-th term that can be divided by M : {fib.div(N, M)}')
         

