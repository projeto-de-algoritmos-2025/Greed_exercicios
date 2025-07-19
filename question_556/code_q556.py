class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        length = len(s)
        pivot_idx = -1
        for i in range(length - 2, -1, -1):
            if s[i] < s[i+1]:
                pivot_idx = i
                break
        if pivot_idx == -1:
            return -1
        successor_idx = -1
        for i in range(length - 1, pivot_idx, -1):
            if s[i] > s[pivot_idx]:
                successor_idx = i
                break
        s[pivot_idx], s[successor_idx] = s[successor_idx], s[pivot_idx]
        left, right = pivot_idx + 1, length - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        result = int("".join(s))
        if result > 2**31 - 1:
            return -1
        return result
