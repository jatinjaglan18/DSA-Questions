class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            hashmap[i] = 1 + hashmap.get(i,0)
            
        l1 = len(hashmap.values())
        l2 = len(set(hashmap.values())) 
        
        return l1 == l2
            