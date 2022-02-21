import math
#https://leetcode.com/problems/fruit-into-baskets/
def fruits_into_baskets(fruits):
  mp = {}
  window_start = 0
  count = 0
  for i in range(len(fruits)):
    fr = fruits[i]
    if fr not in mp:
      mp[fr] = 0
    mp[fr] += 1
    while len(mp) > 2:
      start = fruits[window_start]
      mp[start] -= 1
      if mp[start] == 0:
        del mp[start]
      window_start += 1
    summ = i - window_start + 1
    count = max(summ, count)
  return count