#!/usr/bin/env python
# coding: utf-8

# In[64]:


import heapq

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}



# In[82]:


def prims(graph , start_vertex):
    
    MST = [] 
    
    visited = set()
    visited.add(start_vertex)
    
    
    # create a heap of edges sorted by weight 
    edges = [ (weight , start_vertex , neighbor) for neighbor , weight in graph[start_vertex]]
    heapq.heapify(edges)
    
    #iterate over edges 
    
    while edges:
        weight , u , v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            MST.append((u,v,weight))
        
            for neighbor , weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges , ( weight , v , neighbor ))
            
    
    return MST
    


# In[83]:


prims(graph ,  'A')


# In[127]:


import networkx as nx

def kruskal(graph):
    edges = []
    
    for vertex , neighbors in graph.items():
        for neighbor , weight in neighbors:
            edges.append((vertex , neighbor , weight))

    edges = sorted( edges , key = lambda x : x[2])
    MST = []
    
    uf = nx.utils.UnionFind()
    
    for edge in edges:
        u , v , w  = edge
        
        if uf[u] != uf[v]:
            uf.union(u,v)
            MST.append((u,v,w))
    
    return MST


# In[128]:


kruskal(graph)


# In[ ]:





# In[ ]:





# In[ ]:




