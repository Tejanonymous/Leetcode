class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a={}
        c=set()
        s=list(s.split())
        f=0
        print(a,s)
        if len(pattern)!=len(s):
            return False
        for i in range(len(pattern)):
            if (pattern[i] in a):
                if (a[pattern[i]]==s[i]):
                    continue
                else:
                    f=1
                    break
            else:
                if (s[i] in c):
                    f=1
                    break
                else:
                    a[pattern[i]]=s[i]
                    c.add(s[i])
        print(a,s)
        if f==1:
            return False
        else:
            return True
                
                