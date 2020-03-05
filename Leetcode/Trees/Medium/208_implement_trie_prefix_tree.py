# Runtime: 352 ms, faster than 15.08% of Python online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 40.4 MB, less than 5.88% of Python online submissions for Implement Trie (Prefix Tree).

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