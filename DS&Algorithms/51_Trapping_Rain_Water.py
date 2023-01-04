class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        mx_l = height[l]
        mx_r = height[r]
        ans = 0
        while l < r:
            if mx_l <= mx_r:
                l += 1
                mx_l = max(mx_l, height[l])
                ans += mx_l - height[l]
            else:
                r -= 1
                mx_r = max(mx_r, height[r])
                ans += mx_r - height[r]
        return ans
