class Solution:
    def smallestNumber(self, pattern: str) -> str:

        st = ['1']
        res = ''
        for i in range(len(pattern)):
            if pattern[i] == 'I':
                while st:
                    res += st.pop()
            st.append(chr(i + 1 + ord('1')))
        while st:
            res += st.pop()
        return res