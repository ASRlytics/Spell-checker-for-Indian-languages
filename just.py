######Created by dp#######Reference by norving spell checker#####
from itertools import tee, islice, chain, zip_longest
import itertools
import re
import time
from collections import Counter
#import numpy as np

dp = open('/home/mdp/telugu_corpus.txt').read()
dp1 = dp.split()
dp2 = []
for dp3 in dp1:
    dp2.append(dp3)

#print(dp2)
WORDS = Counter(dp2)

#print(WORDS)

def P(word, N=sum(WORDS.values())):
    ##Probability of `word`.
    return WORDS[word] / N

def correction(word):
    ##Most probable spelling correction for word.
    return max(candidates(word), key=P)

def candidates(word):
    ##Generate possible spelling corrections for word.
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words):
    ##The subset of `words` that appear in the dictionary of WORDS.
    return set(w for w in words if w in WORDS)

def edits1(word):
    ##All edits that are one edit away from `word`.
    letters    = 'అఆఇఈఉఊఋౠఌౡఎఏఐఒఓఔకఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహ ి ా ీ ు ూ ృ ౄ ె ే ై ొ ో ౌ ఁ ం ః ్ ౖ'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    ##All edits that are two edits away from `word`.
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


#print(candidates('అవకతకల'))
print(correction('ఆదర్శవంతమ ైన'))

def text_correction(text):
    start_time = time.time()
    ct = []
    text = text.split()
    for cw in text:
        cor = correction(cw)
        ct.append(cor)
    rt = ' '.join(str(p) for p in ct)
    print("--- %s seconds ---" % (time.time() - start_time))
    return rt

print(text_correction('గత ఏడది ప్రకటచిన ఆంధ్రపరదేశ్ డిఎస్సీ ఫలితాల నియామకలు నేటికీ పూర్తికలేదు అనేక కేసులపై న్యాయపోరటం కొనసగుతోంది'))
print('############################################')

########################bigram correction######################
input = open('/home/mdp/input.txt').read()
txt=input.replace('.',' .')
tokens = txt.split(" ")

unigrams = [(tokens[i]) for i in range(0,len(tokens))]


def remove_element(list_, index_):
    clipboard = []
    for i in range(len(list_)):
        if i is not index_:
            clipboard.append(list_[i])
    return clipboard


def bigram_correction(text):
    word = []
    word1 = []
    word5 = []
    sent = []
    bigrams = [(text[i], text[i + 1]) for i in range(0, len(text) - 1)]
    start_time = time.time()
    for words in bigrams:
        arr = ' '.join(words)
        cword = correction(arr)
        #print("--- %s seconds ---" % (time.time() - start_time))
        out = [item for item in cword.split(' ')]
        print(out)
        word.append(out)
        i=0
    print("--- %s seconds ---" % (time.time() - start_time))
    while i<len(word):
        if i < len(word):
            if len(word[i]) == 1:
                word2 = remove_element(word[i + 1], 0)
                word1.append(word[i])
                word1.append(word2)
                i=i+1
            else: 
                word1.append(word[i])
        i=i+1
    j=0
    for dp9 in word1:
      j=j+1
      if j!=len(word1):
        if len(dp9)==2:
            dp10 = remove_element(dp9, 1)
            word5.append(dp10)
        else: word5.append(dp9)
      else:
            word5.append(dp9)

    word6 = [i for i, j in zip_longest(word5, word5[1:]) if i != j]
    md = list(itertools.chain.from_iterable(word6))
    d = list(map(str.strip, md))
    print(d)
    rt1 = ' '.join(str(p) for p in d)
    return text_correction(rt1)

print(bigram_correction(tokens))