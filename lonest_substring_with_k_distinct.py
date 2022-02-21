#https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        mp = {}
        window_start = 0
        max_len = 0
        for window_end in range(len(s)):
            if s[window_end] not in mp:
                mp[s[window_end]] = 0
            mp[s[window_end]] += 1
            while len(mp) > k:
                window_left = s[window_start]
                mp[window_left] -= 1
                if mp[window_left] == 0:
                    del mp[window_left]
                window_start += 1
                print(window_end , window_start)
            max_len = max(max_len, window_end - window_start + 1)
        return max_len