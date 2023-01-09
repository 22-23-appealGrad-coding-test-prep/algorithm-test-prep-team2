class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]: 
        #             return nums[i]
 
        n = Counter(nums)
        for i in n:
            if(n[i] >= 2):
                return i