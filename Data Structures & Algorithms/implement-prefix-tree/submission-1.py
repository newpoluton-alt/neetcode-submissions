class PrefixTree:

    def __init__(self):
        self.wd = {}
        self.us = set()

    def insert(self, word: str) -> None:
        self.wd[word] = word
        il = ""
        for l in word:
            il += l
            if il not in self.us:
                self.us.add(il)

    def search(self, word: str) -> bool:
        return word in self.wd

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.us
        