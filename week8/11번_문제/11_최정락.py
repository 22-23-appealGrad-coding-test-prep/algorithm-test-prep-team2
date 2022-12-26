class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        r = len(height)-1
        l = 0
        result = 0
        
        while l != r:
            w = r-l
            h = min(height[r], height[l])
            area = w * h
            
            if area > result:
                result = area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return(result)