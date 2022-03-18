#How to make a Tree in Python 
# class Node: 
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.data = data


# root = Node (10)

# root.left = Node(34)
# root.right = Node(89)
# root.left.left = Node(45)
# root.left.right = Node(50)

list=['A','B','C','D']


class Node:
    def __init__(self):
        self.count=0
        self.children={}
    

class Trie:
    def __init__(self):
        self.root=Node()
    
    def insert(self,word):
        curr_node=self.root
        curr_node.data='Nodo Madre'
        list=[curr_node.data]
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node()
                list.append(curr_node.children[c])
            curr_node = curr_node.children[c]
            curr_node.count +=1

        return list

trie = Trie()

print(trie.insert(list)) 