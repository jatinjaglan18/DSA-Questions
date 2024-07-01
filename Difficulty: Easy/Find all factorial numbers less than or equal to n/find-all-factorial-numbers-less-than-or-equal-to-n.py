#User function Template for python3
def fac(n):
    if n == 1:
        return 1
    r = fac(n-1)
    res = n * r
    return res
    
class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	ans = []
    	for i in range(1, n+1):
    	    r = fac(i)
    	    if r > n:
    	        break
    	    else:
    	        ans.append(r)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends