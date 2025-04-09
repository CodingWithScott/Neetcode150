from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        for curr_char in s:
            if curr_char not in s_chars.keys():
                s_chars[curr_char] = 1
            else:
                s_chars[curr_char] = s_chars[curr_char] + 1

        for curr_char in t:
            if curr_char not in t_chars.keys():
                t_chars[curr_char] = 1
            else:
                t_chars[curr_char] = t_chars[curr_char] + 1

        if s_chars == t_chars:
            return True
        return False

s = "racecar" 
t = "carrace"
solution1 = Solution()
print('This should be true: ' + str(solution1.isAnagram(s, t)))

s = "jar" 
t = "jam"
solution2 = Solution()
print('This should be false: ' + str(solution2.isAnagram(s, t)))

s = "xx"
t = "x"
solution3 = Solution()
print('This should be false: ' + str(solution3.isAnagram(s, t)))