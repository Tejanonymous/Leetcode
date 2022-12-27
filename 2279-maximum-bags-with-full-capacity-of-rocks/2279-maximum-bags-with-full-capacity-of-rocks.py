class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        c=0
        for i in range(len(rocks)):
            capacity[i]=capacity[i]-rocks[i]
        capacity.sort()
        i=0
        while additionalRocks!=0 and i<len(capacity):
            if capacity[i]==0:
                c+=1
                i+=1
            else:
                if capacity[i]<=additionalRocks:
                    additionalRocks-=capacity[i]
                    capacity[i]=0
                    i+=1
                    c+=1
                else:
                    break
        
        print(capacity,c,i)
        return c
            
            