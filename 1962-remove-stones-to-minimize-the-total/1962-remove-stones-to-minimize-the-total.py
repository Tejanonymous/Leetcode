from heapq import heappop, heappush, heapify
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles=[-num for num in piles]
        heapq.heapify(piles)
        #by default min heap that means whenever pop we get min element if - we get  
        for i in range(k):
            temp=-heappop(piles)  #we got max number from number 
            
            heappush(piles,-(temp-(temp//2)))
        return -sum(piles)
            