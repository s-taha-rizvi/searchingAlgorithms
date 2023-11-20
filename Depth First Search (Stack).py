# Depth-First Search //Stack

"""Definig Graph using PY Dictionary. Each KEY represents a parent Node and each 
VALUE(given as a list of nodes) represents its child nodes."""
graph={'A':['B','D'],
       'B':['A','C','D'],
       'C':['B'],
       'D':['A','B','G'],
       'G':['D']
       }

""""An empty list named visited to store the nodes once they are treversed."""
visited=[]

''''Passing the start node and the goal node.'''
start,goal='A','C'

"""Initializing stack with the start value. """
stack=[start]

"""While loop that will run until the stack is Empty."""
while(len(stack)!=0):
    """ A pop function is used to get the last entered value in the stack. """
    popped=stack.pop()
    """Checking if the popped node is already visited then the loop starts over."""
    if popped in visited:
        continue
    """Else it prints the popped node and add it to the visited list."""
    print(popped)
    visited.append(popped)
    """Checking if the popped node is the goal then break the loop."""
    if popped==goal:
        break
    """Else adding the Child nodes of the popped node to the stack for further traversing."""
    for i in graph[popped]:
        if i not in visited:
            stack.append(i)
