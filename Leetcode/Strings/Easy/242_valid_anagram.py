# Runtime: 24 ms, faster than 98.03% of Python online submissions for Valid Anagram.
# Memory Usage: 12.9 MB, less than 55.26% of Python online submissions for Valid Anagram.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        map1 = [0 for _ in range(26)]
        map2 = [0 for _ in range(26)]
        
        for i in s:
            map1[ord(i) - 97] += 1
        
        for i in t:
            map2[ord(i) - 97] += 1
        
        map1 = "#".join(map(str, map1))
        map2 = "#".join(map(str, map2))
        
        return map1 == map2