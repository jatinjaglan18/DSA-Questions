#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here
        if A > B:
            l = A
            s = B
        else:
            l = B
            s = A
        
        while l % s != 0:
            rem = l % s
            l = s
            s = rem
        
        gcd = s
        lcm = (A*B) // gcd
        
        return lcm, gcd
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends