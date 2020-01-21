# Runtime: 156 ms, faster than 36.23% of Python online submissions for Candy.
# Memory Usage: 13.8 MB, less than 54.55% of Python online submissions for Candy.

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        n = len(ratings)
        
        a = [1 for _ in ratings]
        b = [1 for _ in ratings]
         
        i = 0
        while i < n:
            j = n-i-1
            
            if i-1 >= 0 and ratings[i]  > ratings[i-1]:
                a[i] = a[i-1] + 1
            
            if j+1 <= n-1 and ratings[j] > ratings[j+1]:
                b[j] = b[j+1] + 1
            
            i += 1
        
        ans = 0
        
        for i in range(n):
            ans += max(a[i], b[i])
        
        return ans