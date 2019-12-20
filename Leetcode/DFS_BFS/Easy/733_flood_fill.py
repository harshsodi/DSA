# Runtime: 64 ms, faster than 54.55% of Python online submissions for Flood Fill.
# Memory Usage: 11.8 MB, less than 81.82% of Python online submissions for Flood Fill.

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
    
        m = len(image)
        if m == 0:
            return image
        
        n = len(image[0])
        
        scolor = image[sr][sc]
        if scolor == newColor:
            return image
        
        
        v = {(sr, sc): True}
        q = [(sr, sc)]
        
        while q:
            top = q.pop(0)
            
            image[top[0]][top[1]] = newColor
            
            if top[0] > 0:
                up = (top[0]-1, top[1])
                if image[up[0]][up[1]] == scolor and v.get(up) == None:
                    q.append(up)
                    v[up] = True
            
            if top[0] < m-1:
                down = (top[0]+1, top[1])
                if image[down[0]][down[1]] == scolor and v.get(down) == None:
                    q.append(down)
                    v[down] = True
        
            
            if top[1] > 0:
                left = (top[0], top[1]-1)
                if image[left[0]][left[1]] == scolor and v.get(left) == None:
                    q.append(left)
                    v[left] = True
                    
            if top[1] < n-1:
                right = (top[0], top[1]+1)
                if image[right[0]][right[1]] == scolor and v.get(right) == None:
                    q.append(right)
                    v[right] = True
                    
        return image