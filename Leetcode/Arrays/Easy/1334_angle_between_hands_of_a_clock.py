# Runtime: 12 ms, faster than 97.42% of Python online submissions for Angle Between Hands of a Clock.
# Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Angle Between Hands of a Clock.

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        
        hr_hr = 30
        hr_min = 0.5
        min_min = 6
        
        min_angle = (minutes * min_min) % 360
        hr_angle = (hour * hr_hr)%360 + (minutes * hr_min)%360
        
        ang1 = abs(hr_angle - min_angle)
        ang2 = 360 - ang1
        
        return min(ang1, ang2)