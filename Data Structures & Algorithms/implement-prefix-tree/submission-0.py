class Trienode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class PrefixTree:

    def __init__(self):
        self.root = Trienode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = Trienode()
            current = current.children[c]
        current.endofword = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.endofword

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True
        
        