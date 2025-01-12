class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False
        open_values = 0
        close_values = 0

        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0' :
                open_values += 1
            else:
                open_values -= 1
            if open_values < 0:
                return False


        for i in range(len(s)-1, -1, -1):
            if s[i] == ')' or locked[i] == '0' :
                close_values += 1
            else:
                close_values -= 1
            if close_values < 0 :
                return False

        return True
