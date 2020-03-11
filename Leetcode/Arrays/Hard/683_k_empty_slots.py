# Your submission beats 33.61% Submissions!

class Solution:
    """
    @param flowers: the place where the flower will open in that day
    @param k:  an integer
    @return: in which day meet the requirements
    """
    def kEmptySlots(self, flowers, k):
        # Write your code here
        
        n = len(flowers)
        
        days = [0 for _ in flowers]
        for i in range(n):
            days[flowers[i]-1] = i
            
        left = 0
        right = k+1
        
        ans = float('inf')
        i = 1
        while right < n:
            
            if days[i] > days[left] and days[i] > days[right]:
                i += 1
                continue
            
            if i == right:
                ans = min(ans, max(days[left], days[right]))
            
            left = i
            right = left + k + 1
            
            i += 1
        
        if ans == float('inf'):
            return -1
        return ans+1