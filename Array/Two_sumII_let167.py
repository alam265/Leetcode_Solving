numbers = [2,3,4] 
target = 6

l = 0 
r = len(numbers)-1 

while l < r: 
    if numbers[l]+numbers[r] == target: 
        print(l, r)
        break
    elif numbers[l]+numbers[r] < target:
        l += 1

    else: 
        r -= 1 


