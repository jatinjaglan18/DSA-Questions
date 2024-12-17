from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char_freq = [list(i) for i in Counter(s).items()]
        char_freq.sort(reverse=True)  # Sort by character (key) in descending order
        
        result = ""  # Resultant string

        while char_freq:
            if char_freq[0][1] > repeatLimit:
                # Append repeatLimit of the largest available character
                result += char_freq[0][0] * repeatLimit
                char_freq[0][1] -= repeatLimit

                # If possible, append the next largest character to "break" the limit
                if len(char_freq) > 1:
                    result += char_freq[1][0]
                    char_freq[1][1] -= 1
                    if char_freq[1][1] == 0:
                        char_freq.pop(1)  # Remove if exhausted
                else:
                    break  # No other character to use, terminate
            else:
                # Append all remaining occurrences of the largest available character
                result += char_freq[0][0] * char_freq[0][1]
                char_freq.pop(0)  # Remove as frequency is exhausted
            
        return result
        