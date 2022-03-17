"""
The difficult part of this problem is to comprehend the problem description.

What the problem says asks is that
        -- if insert() is called, 
                  -- the value will be inserted at idKey-1 in a list/an array;
                  -- the returned list should be from [ptr:last_none_None_val]
            
**Note: ptr is set to 0 at first, and is updated only an unempty list has been returned. 

Data Structure: list (or array if you use other programming language)

time: O(n) where n is the length of the array
space: O(n)
        

"""

class OrderedStream:
    ptr = 0

    def __init__(self, n: int):
        self.n = n
        self.l = [None] * n 

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1] = value
        ordered = []
        if(idKey-1 == self.ptr):
            for i in range(idKey-1, self.n):
                if self.l[i]!=None:
                    ordered.append(self.l[i])
                else:
                    self.ptr = i
                    return ordered
        return ordered
