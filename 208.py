class TrieNode:
    def __init__(self, val, end):
        self.val = val
        self.children = {}
        self.end = end


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(0,False)        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.insertRecur(word, self.root)

    def insertRecur(self, word: str, root: TrieNode):
        if word:
            letter = word[0]
            word = word[1:]
            if letter not in root.children:
                root.children[letter] = TrieNode(letter, not word)
            self.insertRecur(word,root.children[letter])
        else:
            root.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.searchRecur(word, self.root)

    def searchRecur(self, word: str, root: TrieNode):
        if word:
            letter = word[0]
            word = word[1:]
            if letter in root.children:
                return self.searchRecur(word,root.children[letter])
            else:
                return False
        if root and (root.end == True):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.startsWithRecur(prefix, self.root)

    def startsWithRecur(self, prefix: str, root: TrieNode):
        if prefix:
            letter = prefix[0]
            prefix = prefix[1:]
            if letter in root.children:
                return self.startsWithRecur(prefix,root.children[letter])
            else:
                return False
        if root:
            return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("app")
print(obj.search("word"))
print(obj.search("wo"))
print(obj.search("werk"))
#print("yuh")
print(obj.startsWith("we"))