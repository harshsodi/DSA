# Runtime: 48 ms, faster than 77.67% of Python online submissions for Reverse Vowels of a String.
# Memory Usage: 16.4 MB, less than 30.77% of Python online submissions for Reverse Vowels of a String.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = [x for x in s]
        n = len(s)
        a = []
        
        v = {'a':True, 'e':True,'i':True,'o':True,'u':True, 'A':True, 'E':True,'I':True,'O':True,'U':True}
        for i in range(n):
            if v.get(s[i]):
                a.append(i)
        
        m = len(a)
        for i in range(m/2):
            s[a[i]], s[a[m-i-1]] = s[a[m-i-1]], s[a[i]] 
        
        return "".join(s)