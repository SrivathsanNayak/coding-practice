class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        #init two stacks for implementing queue

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #transfer elements from stack1 to stack2
        #then append element to be pushed
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
        
        #now transfer all from stack2 to stack1 back
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        """
        :rtype: int
        """
        #remove last element of stack
        return self.stack1.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        #return last element of stack
        return self.stack1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        #returns True if stack empty
        return not self.stack1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()