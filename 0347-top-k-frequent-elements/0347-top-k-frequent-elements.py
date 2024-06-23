class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        fre = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            d[i] = 1 + d.get(i,0)
        
        for i, j in d.items():
            fre[j].append(i)
        
        res=[]
        for i in range(len(fre)-1,0,-1):
            for j in fre[i]:
                res.append(j)
                if len(res) == k:
                    return res