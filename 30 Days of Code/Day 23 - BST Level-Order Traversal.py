    def levelOrder(self,root):
        q = [root] if root else []
        while q :
            node = q.pop(0)
            print(node.data, end = ' ')
            if node.left :
                q.append(node.left)
            if node.right :
                q.append(node.right)
