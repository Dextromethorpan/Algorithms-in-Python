#STACK 
#A Stack is a linear data structure that stores items in a Last-In/First-Out(LIFO) or First-In/Last-Out(FILO) manner
#In a Stack a new element is added at the one end and an element is removed from that end only. 
#The Insert and Delete operations are often called Push and Pop.

#Python program to demonstrate stack implementation using List
stack=[]

# append() function to push element in the stack 
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

#pop() function to pop element from the stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack )
