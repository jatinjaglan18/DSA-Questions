class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        p = sorted(potions)
        for i in spells:
               
            l = 0
            r = len(p) - 1
            idx = len(p)
            while l <= r:
                m = (l + r) // 2
                if i * p[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            
            res.append(max(len(p)-idx,0))   
                
                    
        return res           
                