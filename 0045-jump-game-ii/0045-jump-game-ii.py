class Solution:
    def jump(self, nums: list[int]) -> int:
        near = far = jumps = 0
        while far < len(nums) -1:
            farther = 0
            for i in range(near,far+1):
                farther = max(farther,i + nums[i])
            near = far + 1
            far = farther
            jumps += 1
        return jumps