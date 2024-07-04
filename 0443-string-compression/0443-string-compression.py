class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        nex = 0
        curr = 0
            
        while curr < n:
            start = chars[curr]
            count = 0 
            while curr < n and chars[curr] == start:
                count += 1
                curr += 1
            
            chars[nex] = start
            nex += 1
            if count > 1 and count < 10:
                chars[nex] = str(count)
                nex += 1 
            
            elif count > 9:
                g_count = str(count)
                for i in range(len(g_count)):
                    chars[nex] = g_count[i]
                    nex += 1
            
        chars = chars[:nex]
            
        return len(chars)