class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wor1={}
        a=[]
        a2=[]
        wor2={}
        
        b=[]
        b2=[]
        for i in word1:
            if i in wor1:
                wor1[i]+=1
            else:
                wor1[i]=1
        for i in word2:
            if i in wor2:
                wor2[i]+=1
            else:
                wor2[i]=1
        for i in wor1:
            a.append(wor1[i])
            a2.append(i)
        for i in wor2:
            b.append(wor2[i])
            b2.append(i)
        print(a,b)
        a.sort()
        a2.sort()
        b.sort()
        b2.sort()
        return a==b and a2==b2