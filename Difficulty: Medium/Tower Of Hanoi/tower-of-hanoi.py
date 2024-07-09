# User function Template for python3
def toh(n,t1,t2,t3,l):
    if n == 0:
        return
    toh(n-1,t1,t3,t2,l)
    print('move disk', n, 'from rod', t1, 'to rod', t2)
    l.append(1)
    toh(n-1,t3,t2,t1,l)
    return len(l)
class Solution:
    def __init__(self):
        self.count = 0 
    
    def toh(self, n, fromm, to, aux):
        # Your code here
        if n == 0:
            return
        
        self.toh(n-1,fromm,aux,to)
        print('move disk', n, 'from rod', fromm, 'to rod', to)
        self.count += 1
        self.toh(n-1,aux,to,fromm)
        
        return self.count

#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends