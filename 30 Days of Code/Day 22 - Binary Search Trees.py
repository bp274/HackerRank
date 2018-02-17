    def getHeight(self,root):
        if root != None :
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        else :
            return -1
