# Depth-First Search //Stack
graph={'A':['B','D'],
       'B':['A','C','D'],
       'C':['B'],
       'D':['A','B','G'],
       'G':['D']
       }

visited=[]

start,goal='A','C'

stack=[start]

while(len(stack)!=0):
    popped=stack.pop()
    if popped in visited:
        continue
    print(popped)
    visited.append(popped)
    if popped==goal:
        break
    for i in graph[popped]:
        if i not in visited:
            stack.append(i)
