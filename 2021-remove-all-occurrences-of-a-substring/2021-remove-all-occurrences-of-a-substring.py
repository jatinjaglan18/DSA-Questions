class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        st = []
        for i in s:
            st.append(i)
            if len(st) >= n and st[-1] == part[-1]:
                if ''.join(st[-n:]) == part:
                    j = 0
                    while j < n:
                        st.pop()
                        j += 1
        return ''.join(st)
        