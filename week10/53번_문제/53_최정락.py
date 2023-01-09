class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        n = 0

        for i in nums:
            if n + i > i:
                n = n + i
            else:
                n = i
            maxsum = max(maxsum,n)
        
        return maxsum