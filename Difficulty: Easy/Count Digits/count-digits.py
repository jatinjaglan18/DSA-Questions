#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        n = N
        count = 0
        while n > 0:
            rem = n % 10
            if rem != 0 :
                if N % rem == 0:
                    count += 1
                
            n = n // 10 
            
        return count    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends