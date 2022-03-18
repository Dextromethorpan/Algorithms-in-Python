#Como programar un Arbol Binario?

#Quiero crear un Arbol Binario que al introducirle su largo L me devuelva un Arbol Binario de largo L

class Tree:
    def __init__(self,x,left=None,right=None):
      self.x=x
      self.left=left
      self.right=right 
    
    def one_tree(self,node):
        node=Tree(1)
        node.right=Tree(1)
        node.left=Tree(1)
        return node
        


node=Tree(1)
node=node.one_tree(node)
L=1

while L>0:
    node=node.one_tree(node)
    node.left=node
    node.right=node
    L=L-1

print(node.right.right.right.right)
