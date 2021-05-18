
def histogram(word):
    d=dict()
    for letter in word:
        d[letter]=d.get(letter,0)+1
    return d

d=histogram('acbbbaac')
#print(histogram('acbbbaac'))

def print_hist(h):
    for c in h:
        print(c,h[c])
    print('-----')
    for key in sorted(h):
        print(key,h[key])
        
#print_hist(d)

def invert_dict(d):
    inverse=dict()
    for key in d:
        val=d[key]
        if val not in inverse:
            inverse[val]=[key]  #[key] mean it`s a list not str
        else:
            inverse[val].append(key)
    return inverse

print_hist(invert_dict(d))