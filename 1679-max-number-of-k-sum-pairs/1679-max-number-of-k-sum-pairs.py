def merge(l,r):
    i = 0
    j = 0
    s_l = []
    while i < len(l) and j < len(r):
        if l[i]<r[j]:
            s_l.append(l[i])
            i += 1
        else:
            s_l.append(r[j])
            j += 1
    
    while i < len(l):
        s_l.append(l[i])
        i += 1
    while j < len(r):
        s_l.append(r[j])
        j += 1
        
    return s_l

def merSort(arr,l,r):
    if r - l <= 1:
        return arr[l:r]
    
    m = (r + l) // 2
    L = merSort(arr,l,m)
    R = merSort(arr,m,r)
    
    return merge(L,R)
    
            
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = merSort(nums,0,len(nums))
        l = 0
        r = len(nums) - 1
        ops = 0
        while l < r:
            num = k - n[l]
            
            if n[r] > num:
                r -= 1
            elif n[r] == num:
                ops += 1
                l+=1
                r-=1
            elif n[r] < num:
                l += 1
                
        return ops