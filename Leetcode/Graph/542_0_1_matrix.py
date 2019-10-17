# Runtime: 872 ms, faster than 16.39% of Python online submissions for 01 Matrix.
# Memory Usage: 15.1 MB, less than 45.45% of Python online submissions for 01 Matrix.

class Solution(object):
        
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        ans = [[sys.maxint for j in i] for i in matrix]

        from collections import deque
        
        for i in range(m):
            for j in range(n):
                # BFS on matrix[i][j]
                visited = {(i,j): True}
                q = deque([(i, j)])
                
                while len(q):
                    
                    t = q.popleft()
                    # visited[t] = True
                    
                    if matrix[t[0]][t[1]] == 0:
                        ans[i][j] = min(ans[i][j], abs(i-t[0]) + abs(j-t[1]))
                        break
                    else:
                        up = (t[0]-1, t[1])
                        down = (t[0]+1, t[1])
                        left = (t[0], t[1]-1)
                        right = (t[0], t[1]+1)
                        
                        ap = [up, down, left, right]
                        
                        if up[0] >= 0 and not visited.get(up):
                            q.append(up)
                            visited[up] = True
                            
                        if down[0] < m and not visited.get(down):
                            q.append(down)
                            visited[down] = True

                        if left[1] >= 0 and not visited.get(left):
                            q.append(left)
                            visited[left] = True
                            
                        if right[1] < n and not visited.get(right):
                            q.append(right)
                            visited[right] = True
                            
        return ans