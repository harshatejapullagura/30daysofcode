#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        for i in range(len(s)):
            if not s[i] in m: #if there is not char in map
                m[s[i]] = 0
            else:
                m[s[i]] += 1 #if there is already a char
        return (len(m))


sl = Solution()
s = "abcabcbb"
print(sl.lengthOfLongestSubstring(s))