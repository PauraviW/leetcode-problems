class TrieNode:
    def __init__(self, val):
        self.value  = val
        self.isFinished = False
        self.children = []
        self.counter = 1


class Trie:
    def __init__(self):
        self.root = TrieNode("*")
        self.list = []

    def add(self, word):

        node = self.root
        for char in word:
            found_in_child = False

            for child in node.children:
                if child.value  == char:
                    child.counter += 1

                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)

                node = new_node
            node.isFinished = True
    def display(self):
        self.l = []
        self.traverse(self.root)
        print(self.l)
    def traverse(self, root):

        if root:
            self.l.append(root.value)
            for child in root.children:
                self.traverse(child)
    def search_prefix(self, prefix):
        node = self.root
        if not node.children:
            return  False
        for char in prefix:
            found = False
            for child in node.children:
                if child.value == char:
                    node = child
                    found = True
                    break
            if not found:
                return False
        return True

    def dictionary(self, word):
        node = self.root
        stack  = [node]
        for char in word:
            found = False
            if stack:
                node = stack.pop(0)
                if char.isalpha():
                    for child in node.children:
                        if child.value == char:
                            found = True
                            stack.append(child)
                            break
                elif char == '.':
                    for child in node.children:
                        stack.append(child)
                        found = True

            if not found and not stack:
                return False
        if node.isFinished:
                return True
        else:
                return False



if __name__ == "__main__":
    trie = Trie()
    # trie.add("buy")
    # trie.add('bull')
    # trie.add('tull')
    # trie.display()
    # # print(trie.search_prefix("gu"))
    # print(trie.dictionary("aa"))
    # # print(find_prefix(root, 'hac'))
    # print(find_prefix(root, 'hack'))
    # print(find_prefix(root, 'hackathon'))
    # print(find_prefix(root, 'ha'))
    # print(find_prefix(root, 'hammer'))
    action = [ "addWord", "addWord", "addWord", "search", "search", "search", "search"]
    key = [ ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    for action, val in zip(action, key):
        if action == 'addWord':
            trie.add(val[0])
        elif action == 'search':
            print(trie.dictionary(val[0]))


