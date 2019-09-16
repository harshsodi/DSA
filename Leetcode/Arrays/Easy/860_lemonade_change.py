# Runtime: 120 ms, faster than 77.11% of Python online submissions for Lemonade Change.
# Memory Usage: 11.9 MB, less than 66.67% of Python online submissions for Lemonade Change.

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        s = 0
        
        d = {
            5: 0,
            10: 0,
            20: 0
        }
        
        for i in bills:
            
            d[i] += 1
            change_req = i-5
            
            if change_req == 15:
                # 10 + 5
                if d[10] > 0:
                    if d[5] == 0:
                        return False
                    d[10] -= 1
                    d[5] -= 1
                    continue
                # 5+5+5
                if d[5] < 3:
                    return False
                d[5] -= 3
                continue
            
            if change_req == 5:
                if d[5] == 0:
                    return False
                d[5] -= 1
                continue
                
        return True