class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        enc_str = ''
        for i in range(len(s)):
            idx = i + k
            if idx >= len(s):
                idx = idx % len(s)
            enc_str += s[idx]
        return enc_str
            
        