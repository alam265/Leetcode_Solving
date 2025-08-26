word1 = "ab"
word2 = "abbxxc"

out = ""

p1 = p2 = 0 

while p1 < len(word1) and  p2 < len(word2):
    out += word1[p1]
    out += word2[p2] 
    p1 += 1
    p2 += 1 


while p1 < len(word1):
    out += word1[p1] 
    p1 += 1
while p2 < len(word2):
    out += word2[p2] 
    p2 += 1


print(out)

