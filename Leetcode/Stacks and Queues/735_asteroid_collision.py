# Runtime: 80 ms, faster than 83.66% of Python online submissions for Asteroid Collision.
# Memory Usage: 12.5 MB, less than 36.36% of Python online submissions for Asteroid Collision.

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        st = []
        
        for a in asteroids:
            while len(st) and a < 0 and st[-1] > 0:
                
                if a == None:
                    break
                
                if st[-1] < -a:
                    st.pop()
                elif st[-1] > -a:
                    a = None
                elif st[-1] == -a:
                    st.pop()
                    a = None
            
            if a != None:
                st.append(a)
            
        return st