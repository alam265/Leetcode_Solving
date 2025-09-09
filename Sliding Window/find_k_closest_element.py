class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        res = []

        for i in range(len(arr)): 
            heapq.heappush(pq, ((abs(arr[i] - x)), arr[i]))  


        for j in range(k):
            res.append(heapq.heappop(pq)[1]) 

        res.sort() 

        return res