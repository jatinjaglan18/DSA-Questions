class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        ans[-1] = n
        if A[0] == B[0]:
            ans[0] = 1

        for i in range(1,n-1):
            if A[i] == B[i]:
                ans[i]=ans[i-1]+1
                continue
            count = 0
            if A[i] in B[:i]:
                count += 1
            if B[i] in A[:i]:
                count += 1
            ans[i] = ans[i-1] + count
        return ans