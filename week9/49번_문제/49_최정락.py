class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}        
        
        for i in strs:
            string = "".join(sorted(i))
            if string not in d:
                d[string] = [i]            
            else:
                d[string].append(i)                
        
        return d.values()