class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if len(points) == 0: return 0 
        
        points.sort(key = lambda x: x[1])
        arrow=1
        
        pointer=points[0][1]
        for i in points:
            print(pointer,i[0])
            if pointer < i[0]:
                arrow+=1
                pointer=i[1]
        
        print(arrow)
        return arrow