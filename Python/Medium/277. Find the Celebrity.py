# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(0, n):
            flag = True
            for j in range(0, n):
                if j == i:
                    continue
                flag = flag and not knows(i, j) and knows(j, i)
            if flag:
                return i
            
        return -1


        x = 0
        for i in range(n):
            if knows(x, i):
                x = i
        
        for i in range(x):
            if knows(x, i):
                return -1
        
        for i in range(n):
            if not knows(i, x):
                return -1
            