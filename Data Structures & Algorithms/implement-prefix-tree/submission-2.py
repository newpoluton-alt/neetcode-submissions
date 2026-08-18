class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.endOfWord = True
    
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    # def __init__(self):
    #     self.wd = {}
    #     self.us = set()

    # def insert(self, word: str) -> None:
    #     self.wd[word] = word
    #     il = ""
    #     for l in word:
    #         il += l
    #         if il not in self.us:
    #             self.us.add(il)

    # def search(self, word: str) -> bool:
    #     return word in self.wd

    # def startsWith(self, prefix: str) -> bool:
    #     return prefix in self.us
        