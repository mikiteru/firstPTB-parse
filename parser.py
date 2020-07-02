import re
import nltk
def lappend(a,k,w):
    if(len(a)<=k):
        a.append(w)
    else:
        a[k]+=w
def wordcount(sen):
    num = 0
    inword = True
    for i in sen:
        if (i == "("):
            inword = True
        elif ((i == ")") and (inword)):
            num += 1
            inword = False
    return(num)
ptb = open("ptbtree.txt")
voc = open("vocabrally.txt",mode = "w")
stack = []
#vocabulary = {}
stack_num = 0

s = ptb.readlines()

for i in range(len(s)):
    s[i]=s[i].replace('\n','')      #改行文字を取り除く

ex = "(S (NP (NNP John))(VP (VBZ loves)(NP (NNP Mary)))(. .))"
#print(s[1])
for i in ex:      #文を扱いやすいように分解(本当に必要だったかは要検討)
    if (i=="("):
        if(stack_num>=len(stack)):
            stack.append(i)
            stack_num += 1
        else:
            stack[stack_num] += i
            stack_num += 1
    else:
        stack[stack_num-1]+=i
print(stack)
'''
for ss in s:
    word = re.findall(r"([A-Za-z0-9',=.`$\-]+) ([A-Za-z0-9'\*,.`$\-]+)",ss)   #文全体の各単語と品詞の組み合わせ
    for w in word:
        voc.write(w[0] + " , " + w[1] + "\n")
'''
k=0
dic={}      #各品詞や，単語がどの単語からどの単語まで，何単語目から何単語目までカバーしているかを格納していく
p = 1   #タグがカバーする単語の初めの位置

for i in range(0,len(stack)):
    flag = 0
    list = []       #list[0]に品詞，list[1]にそれがカバーする初めの単語(ただの単語の場合はその単語)，list[2]に終わりの単語
    rb = 0      #右かっこの数
    sflag = 1   #そのタグの範囲の初まり
    eflag = 0   #そのタグの範囲の終わり
    spanflag=True      #左かっこが出るとTrue，その後右かっこが出るとFalseにしてタグがカバーしている単語数を増やす
    span=0      #何単語をカバーしているかを示す
    for x in stack[i:len(stack)]:
        for l in x:
            if(flag==0):
                if(l == "("):
                    flag = 1    #解析開始
                    tflag = 1   #タグの部分であることを示す
                    lb=1        #左かっこの数
            else:
                if(l == "("):
                    lb += 1
                    if(sflag and (len(list)>1)):
                        list.remove(list[1])
                    elif(eflag and (len(list)>2)):
                        list.remove(list[2])
                    spanflag = True
                elif(l == ")"):
                    rb += 1
                    sflag = 0
                    eflag = 1
                    if(spanflag == True):
                        span+=1
                        spanflag = False
                else:
                    if(tflag):
                        if (l == " "):      #空白が出てきたらタグの範囲終了
                            tflag = 0
                        else:
                            lappend(list,0,l)
                    else:
                        if(sflag):
                            lappend(list,1,l)
                        if(eflag):
                            lappend(list,2,l)
                if(lb<=rb):     #右かっこの数が左かっこの数以上になったら抜ける
                    break
        if(lb<=rb):         #上同
            break
    span -= 1               #p始まりで単語数がspanのため範囲としてはp文字目からp+span-1文字目まで
    if(len(list)>2):                #listに三つめが存在(二つ以上の単語を含むタグ)
        dic[k] = [list[0],(list[1],p),(list[2],p+span),p,p+span]
    elif(lb>1):                     #左かっこが二つ以上存在=一つの単語を含むタグ(単語ではない)
        dic[k] = [list[0],(list[1],p),(list[1],p),p,p]
    else:                           #単語(dic[k][2]は単語の場合は0とする)
        dic[k] = [list[0],(list[1],p),0,p,p]
        p+=1                #単語を解析するたびに範囲の始まりを一つずらす
    k += 1                  #dicの追加する位置を移動
print(dic)

for tag in dic:
    print(dic[tag][0] + " :"+str(dic[tag][3])+"-"+str(dic[tag][4]))

voc.close()
ptb.close()