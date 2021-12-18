class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        count = 0
        current = x
        for i in range(1, x):
            if i % 2 != 0:
                if current == 0:
                    break
                elif current >= i:
                    current -= i
                    count += 1
                else:
                    break
        return count


sl = Solution()
target = 9
print(sl.mySqrt(target))
