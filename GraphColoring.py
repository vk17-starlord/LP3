#!/usr/bin/env python
# coding: utf-8

# In[3]:


def is_valid(graph, node, solution, color):
    # Check if the given color is valid for the given node
    for neighbor in graph[node]:
        #visit neighbor and check if color is same as neighbor's color
        if solution[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors):
    num_nodes = len(graph)
    solution = [-1] * num_nodes
    
    def backtracking(node):
        # base case 
        
        if node >= num_nodes:
            return True
        
        # try all available colors
        
        for color in colors:
            if is_valid(graph,node,solution,color):
                solution[node] = color
                # recursive callback to assign colors
                if backtracking(node+1):
                    return True
                # cleanup 
                solution[node]=-1
                
        return False
    
    if(backtracking(0)):
        return solution
    else:
        return None


# In[4]:


# Example usage:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

colors = ['r', 'g', 'b']

solution = graph_coloring(graph, colors)

if solution is not None:
    print("Solution:", solution)
else:
    print("No solution exists.")


# In[ ]:





# In[ ]:




