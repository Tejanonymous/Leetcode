class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        a={}
        c=0
        for i in tasks:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in a:
            if a[i]==1:
                return -1
            if a[i]%3==0:
                c+=a[i]//3
            else:
                c+=(a[i]//3)+1
        return c
                