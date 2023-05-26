#!/usr/bin/env python
# coding: utf-8

# In[2]:


def job_sequencing(jobs):
    #sort jobs 
    
    jobs.sort(key=lambda x:x[2] , reverse=True)
    
    max_deadline = max(jobs , key=lambda x:x[1])[1]
    
    time_slots = [False]*max_deadline
    results = [None]*max_deadline
    
    #iterate over jobs
    for job in jobs:
        
        for i in range(job[1]-1,-1,-1):
            if not time_slots[i]:
                time_slots[i]=True,
                results[i]=job[0]
                break;
                
    ans=[]
    for i in range(max_deadline):
        if results[i] is not None:
            ans.append(jobs[results[i]-1][0])
                 
    return ans


# In[3]:


jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1,25),(5, 3,15)]


# In[4]:


ans = job_sequencing(jobs)


# In[5]:


ans


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




