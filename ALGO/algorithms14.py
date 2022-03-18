"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced

A height-balanced binary tree is a binary tree in which the 
left and the right subtrees of every node differ in height by
no more than 1.
"""

#Definition for a binary tree node.
class TreeNode:
  def __init__(self,x):
      self.val=x
      self.left=None
      self.right=None

class Solution:
    def isBalanced(self, root:TreeNode)->bool:
        def isBalancedHelper(root):
            if root== None:
                return(True, 0)
            leftB,leftH = isBalancedHelper(root.left)
            rightB,rightH = isBalancedHelper(root.right)
            return (leftB and rightB and abs(leftH-rightH)
                    <=1,max(leftH, rightH)+1)
        return isBalancedHelper(root)[0]

#Preguntas:
#1.Como sabe la function isBalanced() cual es la estructura
#  del Arbol?.
#2.La clase TreeNode contiene toda la información del Arbol 
#  Binario?.