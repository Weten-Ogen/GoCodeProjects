
class Array:
    def __init__(self,n=[]) -> None:
        self.ans = n
         
    def isempty(self):
        return len(self.ans) == 0
    
    def length(self):
        return len(self.ans)
    
    def endpop(self):
        # check if the array  isempty
        if self.isempty():
            return 
        newarr = []
        # removing element fromthe endofthe array
        for i in range(len(self.ans)):
            if i != (len(self.ans) - 1):
                newarr.append(self.ans[i])
            else:
                break
        self.ans = newarr
        return self.ans
            
        

    def endadd(self,x):
        if self.isempty():
            return
        self.ans.append(x)
        return self.ans
        
    def arrlen(self):
        pass

num = Array([1,2,3])
print(num.endadd(25))
# add and remove to the end of the element
# length of array
# how remove and add to the front array
#  check if the arrray is empty 

# set 
# dict 
# tuples
# linked list 
# tree
# graphs
# queues
# LIFO => LAST IN FIRST OUT
# ABSTRACT DATA STRUCTURE 
# FIFO => FIRST IN FIRST OUT


# algorithms
# searching
# linear search
# binary search
# sorting
# breath first search
# depth first search
# divide and conquer
# recursion
#      programming
# asymptotic notation analysis
# big 0 notation 
# O(n) => linear time
# 0(1) => constant time
# 0(log(n)) => logarithmic time
