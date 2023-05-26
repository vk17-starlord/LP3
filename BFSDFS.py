#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[17]:


# graph to visit
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# In[18]:


def bfs(graph,start):
    queue=[start]
    visited=set()
   
    while queue:
        #pop first item in the queue 
        node = queue.pop(0)
        if(node in visited):
            continue 
   
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
        
    return visited


# In[19]:


visited = bfs(graph,'A')


# In[20]:


visited


# In[ ]:





# In[21]:


def dfs(graph,start,visited=None):
    if(visited==None):
        visited=set()
        
    if(start in visited):
        return 
    
    visited.add(start)
    print(start)
    
    stack = [start]
    
    for neighbor in graph[start]:
        if(neighbor not in visited):
            dfs(graph,neighbor,visited)


# In[22]:


dfs(graph,'A')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




