class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            dist = math.sqrt((point[0]-0)**2 + (point[1]-0)**2)
            heapq.heappush(pq, [dist, point[0], point[1]]) 


        res = [] 

        for i in range(k): 
            point_with_dist = heapq.heappop(pq) 
            point =[point_with_dist[1], point_with_dist[2]] 
            res.append(point) 

        return res