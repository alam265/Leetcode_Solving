

def merge(arr, l, m, r): 
    left = arr[l:m+1]
    right = arr[m+1: r+1] 
    i = l 
    p1 = 0 
    p2 = 0 

    while p1 < len(left) and p2 < len(right): 
        if left[p1] <= right[p2]: 
            arr[i] = left[p1]
            p1 += 1 
        else: 
            arr[i] = right[p2]
            p2 += 1 

        i += 1 

    while p1 < len(left): 
        arr[i] = left[p1] 
        p1 += 1
        i += 1
    while p2 < len(right): 
        arr[i] = right[p2] 
        p2 += 1
        i += 1
        





def mergeSort(arr, l, r):
    if l == r:
        return arr 
    m = (l+r) // 2
    mergeSort(arr, l, m) 
    mergeSort(arr, m+1, r) 
    merge(arr, l, m, r)
    return arr

arr = [5,9,0,34,1,-1] 
print(mergeSort(arr, 0, len(arr)-1))



"""Easy to grasp"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return merge_sort(nums)
            