class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        c=0
        maxi=0
        alpha="abcdefghijklmnopqrstuvwxyz"
        a=""
        for i in s:
        
            if a+i in alpha:
                c+=1
                a+=i
            else:
                a=i
                
                maxi=max(c,maxi)
                c=1
        maxi=max(c,maxi)
        return maxi
                
        