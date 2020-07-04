from nltk.tree import Tree
from nltk.stem import WordNetLemmatizer
from nltk.corpus import treebank
import nltk
#import nltk
#nltkのライブラリは((S (...)) )ってなってるの対応してないから(S (...))の方が正しいっぽいか？

#nltk.download('averaged_perceptron_tagger')

def ptb_read(txt):
    k = open(txt)
    sentences = k.readlines()
    for i in range(len(sentences)):
        sentences[i] = sentences[i].replace('\n','')
    k.close()
    return sentences

lemmatizer = WordNetLemmatizer()
st = "getting"
x = treebank.parsed_sents('wsj_0001.mrg')[0]
s = ptb_read("ptbtree.txt")

t = Tree.fromstring(s[0])
vp = Tree('VP',[Tree('V', ['saw'])])

'''for i in t.treepositions('leaves'):
    print(i)
print(t.leaves())'''

t = "(S (NP (NNP John))(VP (VBZ loves)(NP (NNP Mary)))(. .))"
s = "(NP You)"
#t = "I ate a fish and John roast beef."
#morph = nltk.word_tokenize(t)
#pos = nltk.pos_tag(morph)
#print(pos)

def getspan_fromtree(t: 'str of tree') \
        -> 'span of each tag:dictionary{tag_num:(pos,start,end)})':
    tree = Tree.fromstring(t)
    span ={}
    tag_num = 1
    pl=0            #単語の位置
    for i in tree.subtrees():      #部分木すべてについて
        pl = pl+tree.leaves()[pl:].index(i.leaves()[0])       #単語の見る位置を部分木の初めの単語の位置に変更
        start = pl+tree.leaves()[pl:].index(i.leaves()[0])     #タグが含む範囲の初めの位置
        end = start+len(i.leaves())                         #タグが含む範囲の終わりの位置(初めの位置+部分木の葉の数)
        span[tag_num] = (i.label(),start+1,end)
        tag_num += 1
    return(span)
x = getspan_fromtree(t)
print(getspan_fromtree(s))
print(x)
#t.draw()
"""
a=['A','B','A','B']
print(2+a[2:].index('B'))
"""
'''
print(t[0])
print(t.leaves())
print(t.label())
print(t.productions())
print(t.set_label("T"))
print(lemmatizer.lemmatize(st))
print(vp)
'''