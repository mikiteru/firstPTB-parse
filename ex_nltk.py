from nltk.tree import Tree
from nltk.stem import WordNetLemmatizer
from nltk.corpus import treebank
#import nltk
#nltkのライブラリは((S (...)) )ってなってるの対応してないから(S (...))の方が正しいっぽいか？

#nltk.download('id')
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

#t = Tree.fromstring("(S (NP (NNP John))(VP (VBZ loves)(NP (NNP Mary)))(. .))")
pl=0            #単語の位置
for i in t.subtrees():      #部分木すべてについて
    pl = pl+t.leaves()[pl:].index(i.leaves()[0])       #単語の見る位置を部分木の初めの単語の位置に変更
    start = pl+t.leaves()[pl:].index(i.leaves()[0])     #タグが含む範囲の初めの位置
    end = start+len(i.leaves())                         #タグが含む範囲の終わりの位置(初めの位置+部分木の葉の数)
    print(i.label(),start+1,end)
t.draw()
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