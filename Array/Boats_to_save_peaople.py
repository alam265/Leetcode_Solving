
        
people = [3,5,3,4]
limit = 5

people.sort() 

l, r = 0, len(people)-1 

c = 0

while l <= r: 
    if people[l] + people[r] <= limit: 
        l+=1 
        r-=1 
        c+=1
    else: 
        r -= 1
        c+=1

print(c)