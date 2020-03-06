# Runtime: 2968 ms, faster than 5.09% of Python online submissions for Word Search II.
# Memory Usage: 49.9 MB, less than 8.70% of Python online submissions for Word Search II.

class TrieNode(object):
    
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isItEnd = False
        
    def setEnd(self):
        self.isItEnd = True
    
    def isEnd(self):
        return self.isItEnd

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        root = self.root
        
        for i in range(len(word)):
            ch = word[i]
            
            if root.children[ord(ch) - ord('a')] == None:
                root.children[ord(ch) - ord('a')] = TrieNode()
            
            root = root.children[ord(ch) - ord('a')]

        root.setEnd()
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        root = self.root
        for i in range(len(word)):
            ch = word[i]
            
            if root.children[ord(ch) - ord('a')] == None:
                return False
            
            root = root.children[ord(ch) - ord('a')]
        
        if root.isEnd():
            return True
        return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        root = self.root
        for i in range(len(prefix)):
            ch = prefix[i]
            
            if root.children[ord(ch) - ord('a')] == None:
                return False
            
            root = root.children[ord(ch) - ord('a')]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        
        # Enter all words in the dictionary to the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = {}
        
        for i in range(m):
            for j in range(n):
                
                # Do bfs from this cell
                q = [[(i, j), ""+board[i][j], [(i, j)]]]
                
                while len(q):
                    
                    # print q
                    
                    top = q.pop(0)
                    cell = top[0]
                    word = top[1]
                    path = top[2]  
                        
                    if trie.search(word):
                        ans[word] = True
                    
                    if cell[1] > 0:
                        left = (cell[0], cell[1]-1)
                        nxtw = word + board[left[0]][left[1]]
                    
                        if trie.startsWith(nxtw):
                            if left not in path:
                                q.append([left, nxtw, path + [left]])
                
                    if cell[1] < n-1:
                        right = (cell[0], cell[1]+1)
                        # print right
                        nxtw = word + board[right[0]][right[1]]
                    
                        if trie.startsWith(nxtw):
                            if right not in path:
                                q.append([right, nxtw, path+[right]])
                    
                    if cell[0] > 0:
                        up = (cell[0] - 1, cell[1])
                        nxtw = word + board[up[0]][up[1]]
                    
                        if trie.startsWith(nxtw):
                            if up not in path:
                                q.append([up, nxtw, path + [up]])
                    
                    if cell[0] < m-1:
                        down = (cell[0] + 1, cell[1])
                        nxtw = word + board[down[0]][down[1]]
                
                        if trie.startsWith(nxtw):
                            if down not in path:
                                q.append([down, nxtw, path + [down]])
                            
        return ans.keys()