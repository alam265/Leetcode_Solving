
def is_alphabate(char): 
    return (ord("A") <= ord(char) <= ord("Z") or  ord("a") <= ord(char) <= ord("z") or ord("0") <= ord(char) <= ord("9") )

def fun(string):
    p1 = 0
    p2 = len(string)-1 

    while p1 < p2: 
        while p1 < p2 and not is_alphabate(string[p1]) :
            p1 += 1 
        while p1 < p2 and not is_alphabate(string[p2]) :
            p2 -= 1 
        
        if string[p1].lower() != string[p2].lower(): 
            return False
        p1 += 1
        p2 -= 1
    return True 




string = "tab a cat"

        
print(fun(string))
    



