class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 
        total = len(A) + len(B)
        half = total // 2
        
        if len(A) > len(B): 
            A, B = B, A 


        l, r = 0, len(A)-1 
        while True: 
            midA = (l+r) // 2 
            j = half - midA - 2  

            Aleft = A[midA] if midA >= 0 else float("-inf")
            Aright = A[midA+1] if (midA+1) < len(A) else float("inf")
            Bleft = B[j]    if j >=0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf") 

            if Aleft <= Bright and Bleft <= Aright: 
                if total % 2 == 0: 
                    return (max(Aleft, Bleft) + min(Bright, Aright)) / 2 
                else: 
                    return min(Aright, Bright) 

            elif Aleft > Bright: 
                r = midA - 1
                
            else: 
                l = midA + 1 

