
"""Brute Force"""
class FreqStack:

    def __init__(self):
        self.stack = [] 
        self.dic = defaultdict(int)

    def push(self, val: int) -> None:
            self.stack.append(val) 
            self.dic[val] += 1


    def pop(self) -> int:
        maxVal = max(self.dic.values()) 
        i = len(self.stack)-1 

        while self.dic[self.stack[i]] != maxVal: 
            i -=  1 
        self.dic[self.stack[i]] -=  1 
        return self.stack.pop(i) 


"""Optimal"""
class FreqStack:

    def __init__(self):
        self.freq = {} 
        self.maxCnt = 0 
        self.stacks = {} 


    def push(self, val: int) -> None:
        valCnt = 1 + self.freq.get(val, 0) 
        self.freq[val] = valCnt
        
        if valCnt > self.maxCnt: 
            self.maxCnt = valCnt 
            self.stacks[valCnt] = [] 

        self.stacks[valCnt].append(val) 




    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop() 
        self.freq[res] -= 1 
        if not self.stacks[self.maxCnt]:  #if Empty 
            self.maxCnt -= 1 

        return res





            

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

        