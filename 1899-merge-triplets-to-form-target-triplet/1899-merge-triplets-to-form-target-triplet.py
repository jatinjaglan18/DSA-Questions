class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        temp = [False, False, False]
        x,y,z = target
        for a,b,c in triplets:
            if a==x and b<=y and c<=z:
                temp[0] = True
            if b==y and a<=x and c<=z:
                temp[1] = True
            if c==z and a<=x and b<=y:
                temp[2] = True
            if all(temp): return True
        
        return all(temp)