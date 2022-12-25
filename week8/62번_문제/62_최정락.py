class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        list = [[1]*n]*m
        
        for i in range(1,m):
            for j in range(1,n):
                list[i][j] = list[i-1][j] + list[i][j-1]
    
        return list[m-1][n-1]