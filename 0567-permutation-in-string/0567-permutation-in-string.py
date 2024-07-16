class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        '''left = 0
        right = len(s1)
        ss_1 = sorted(s1)
        
        while right < len(s2) + 1:
            string = s2[left:right]
            s_string = sorted(string)
            
            if ss_1 == s_string:
                return True
            
            right += 1
            left += 1
        return False'''
        
        map_1 = {}
        map_2 = {}
        
        for i in range(len(s1)):
            map_1[s1[i]] = 1 + map_1.get(s1[i],0)
            map_2[s2[i]] = 1 + map_2.get(s2[i],0)
            
        if map_1 == map_2:
            return True
        l = 0
        for r in range(len(s1),len(s2)):
            if map_2[s2[l]] == 1:
                del  map_2[s2[l]]
            else:
                map_2[s2[l]]-= 1
            l += 1
            map_2[s2[r]] = 1 + map_2.get(s2[r], 0)
            if map_1 == map_2:
                return True
        
        return False
            
        