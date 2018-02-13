class Solution:
    def __init__(self) :
        self.stack = list()
        self.queue = list()

    def pushCharacter(self, ch) :
        self.stack.append(ch)

    def enqueueCharacter(self, ch) :
        self.queue.append(ch)

    def popCharacter(self) :
        return self.stack.pop()

    def dequeueCharacter(self) :
        return self.queue.pop(0)
