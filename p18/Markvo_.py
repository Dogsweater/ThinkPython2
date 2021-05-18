import sys
import string
import random


class Markvo:
    def __init__(self):
        self.suffix_map={}
        self.prefix=()
    
    def process_file(self,filename,order=2):
        fp=open(filename)
        for line in fp:
            if line.startswith('*** START OF THIS'):
                break
        for line in fp:
            if line.startswith('*** END OF THIS'): 
                break
            for word in line.rstrip().split():
                self.process_word(word, order)
                
    def process_word(self,word, order=2):

        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]

        self.prefix = shift(self.prefix,word)
        
    def random_text(self,n=100):
        # choose a random prefix (not weighted by frequency)
        start = random.choice(list(self.suffix_map.keys()))
        
        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                random_text(n-i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print(word, end=' ')
            start = shift(start, word)

def shift(t, word):
    return t[1:] + (word,)


markvo=Markvo()
markvo.process_file('215.txt')
markvo.random_text()
print()