class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtracking(index, comb, total):
            if total == target:
                ans.append(comb[:])
                return 
            
            for i in range(index,len(candidates)):
                n_total = total + candidates[i]
                
                if n_total > target:
                    return
                    
                comb.append(candidates[i])
                backtracking(i,comb,n_total)
                comb.pop()
                
        backtracking(0,[],0)
        return ans
            