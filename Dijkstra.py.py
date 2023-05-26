#!/usr/bin/env python
# coding: utf-8

# In[2]:


import heapq

def dijkstra(graph,start_vertex):
    #intialize distances array to infinity 
    distances = { vertex:float('inf') for vertex in graph}
    #intialize start vertex distance to 0
    distances[start_vertex] = 0
    # intialize a empty visited list to track nodes which have minimum distance from start 
    visited=set()
    
    queue = [ (0 , start_vertex)]
    
    while queue:
        #extract current distance , current vertex which is minimum among all
        current_distance , current_vertex = heapq.heappop(queue)
        
        #check if it is visited 
        if current_vertex in visited:
            continue 
        # else add it in the visited list 
        visited.add(current_vertex)
        
        for neighbor , weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue,(distance , neighbor))
    
    return distances
        


# In[3]:


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
distances


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




