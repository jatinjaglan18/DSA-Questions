class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        f = []
        p = []
        l = []
        for i in nums:
            if i < pivot:
                f.append(i)
            elif i > pivot:
                l.append(i)
            else:
                p.append(i)
        
        return f + p + l