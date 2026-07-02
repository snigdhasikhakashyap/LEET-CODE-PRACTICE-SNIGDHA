class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            current = roman[s[i]]
            if i + 1 < len(s):
                next_val = roman[s[i+1]]
            else: next_val = 0
            if current < next_val:
                total = total - current
            else: total = total + current
        return total
