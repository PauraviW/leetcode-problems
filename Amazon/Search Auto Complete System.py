from collections import defaultdict


class Node:
    def __init__(self, val=None, freq=0, children= None, sentenceList= [], defauldict=None):
        self.children = defaultdict(Node)
        self.sentenceList = sentenceList
class AutoComplete:
    def __init__(self, sentences, times):
        self.curr= ''
        self.sentenceToFreq = defaultdict(int)
        self.preprocessing(sentences, times)
        self.root = Node()
    def preprocessing(self, sentences, times):
        for i in range(len(sentences)):
            self.sentenceToFreq[sentences[i]] = times[i]
            curr = self.root
            for char in sentences[i]:
                curr.sentenceList.append(sentences[i])
                curr = curr.children[char]
    def input(self, char):
        if char =='#':
            if self.curr not in self.sentenceToFreq:
                self.sentenceToFreq[self.curr] = 1
                curr = self.root
                for char in self.curr:
                    curr.sentenceList.append(self.curr)
                    curr = curr.children[char]
            self.curr = ''
            return []
        else:
            self.curr += char
            curr = self.root
            for char in self.curr:
                curr = curr.children[char]
            st = curr.sentenceList
            return sorted(curr.sentenceList, key = lambda x:-self.sentenceToFreq[x])[:3]



