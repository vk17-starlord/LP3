#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


arr=[1,4,3,2,5]


# In[4]:


def selectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        
        for j in range(i+1 , len(arr)):
            if(arr[j]<arr[min_index]):
                min_index = j
        
        arr[min_index],arr[i] = arr[i] , arr[min_index]


# In[5]:


selectionSort(arr)


# In[6]:


arr


# In[ ]:





# In[48]:





# In[ ]:





# In[ ]:





# In[ ]:




