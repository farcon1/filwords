# -*- coding: utf-8 -*-
def find1(l):
    alph=["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    slov=[]
    #file1 = open("rus1.txt", "r")
    file1 = open("russian1.txt", "r")
    while True:
        line = file1.readline()
        if not line:
            break
        slov.append(line.strip())
    file1.close()
    slov_alph=[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for i in range(len(slov)):
        for g in range(len(alph)):
            if slov[i][0]==alph[g]:
                slov_alph[g].append(slov[i])
    result=[]
    print("______")
    for i in range(len(l)):
        if i%3000==0:
            print(str(round(100*i/len(l),2))+"%")
        q=l[i][0]
        for g in range(len(alph)):
            if alph[g]==q:
                if l[i] in slov_alph[g]:
                    result.append(l[i])
    return result

def komb(q=3):
    b=["U","D","R","L"]
    res=b.copy()
    a=0
    while a<q-1:
        a=len(res[-1])
        ad=len(res)
        for i in range(ad):
            for g in b:
                #print(g)
                res.append(res[i]+g)
    res=list(set(res))
    for i in range(len(res)-1,-1,-1):
        if len(res[i])<2:
            res.pop(i)
    return res

def test_komb(l,comb,i,g):
    y=i+1
    x=g+1
    #print(y,x)
    l[y][x]=0
    for el in range(len(comb)):
        elem=comb[el]
        if elem=="U":
            if l[y-1][x]==0:
                return False
            y-=1
            l[y][x]=0
        elif elem=="D":
            if l[y+1][x]==0:            
                return False
            y+=1
            l[y][x]=0 
        elif elem=="R":
            if l[y][x+1]==0:
                return False
            x+=1
            l[y][x]=0
        elif elem=="L":
            if l[y][x-1]==0:              
                return False
            x-=1
            l[y][x]=0  
    return True

def make_new(ln):
    l=[]
    l.append([0]*(ln+2))
    for a in range(ln):
        l.append([0]+[1]*ln+[0])
    l.append([0]*(ln+2))
    return l
    
def paths(ln,i=0,g=0):
    c_i=i
    c_g=g
    l=[]
    result=[]
    l.append([0]*(ln+2))
    for a in range(ln):
        l.append([0]+[1]*ln+[0])
    l.append([0]*(ln+2))
    for q in range(4,8):
        ks=komb(q) #комбинации для каждой длины слова
        for w in range(len(ks)):
            i=c_i
            g=c_g
            l=make_new(ln)
            if test_komb(l,ks[w],i,g):      
                result.append(ks[w])
                
    return result
def to_word(l,comb,i=0,g=0):
    s=l[i][g]
    q=i
    w=g
    for t in range(len(comb)):
        x=comb[t]
        if x=="U":
            q-=1
            s+=l[q][w]
        elif x=="D":
            q+=1
            s+=l[q][w]
        elif x=="R":
            w+=1
            s+=l[q][w]
        elif x=="L":
            w-=1
            s+=l[q][w]  
    return s
#l=[["и","к","д"],
#   ["т","л","ё"],
#   ["д","у","б"]]
l=[]
print("Введите все буквы построчно:")
first=input()
l.append(list(first))
for i in range(len(first)-1):
    l.append(list(input()))
#print(l)
#for elem in l:
#    print(elem)
"""
ещенетие
лбгитоки
ьаогмщен
тнлкавтс
оецваомр
пнсенрае
аорамтмт
лфачемас

жятьлапс
кадоптио
гббдоюкг
аиогмлпо
лшлуркул
анлещсть
ыседрола
втршокод

икд
тлё
дуб
"""

"""
slov=[]
file1 = open("rus.txt", "r")
while True:
    line = file1.readline()
    if not line:
        break
    slov.append(line.strip())
file1.close()
"""
def need(l):
    l1=sorted(l, key=len)
    l1.reverse()
    return l1

n=len(l)
res=[]
import time
p=[]
t1=time.time()
for i in range(len(l)):
    for g in range(len(l)):
        print(str((g+1)+(i)*len(l))+"/"+str(len(l)**2))
        pths=paths(n,i,g)
        
        for el in pths:
            #n+=1
            #print(str(n)+"/"+str(len(spth)))
            sl=to_word(l,el,i,g)
            res.append(sl)
            p.append(sl)
answers=need(list(set(find1(p))))
print(answers)
t2=time.time()
print("Программа сработала за",round(t2-t1,2),"секунд")
