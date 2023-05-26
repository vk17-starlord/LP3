#!/usr/bin/env python
# coding: utf-8

# In[7]:


import nltk

from nltk.chat.util import Chat,reflections


pairs = [
    
    
    [
        r"hi|hello|how are you ?",
        ["Hello Welcome to the red bus , how can i assist you ?"]
    ]
      ,  
    [
        r"(.*)",
        ["i'm sorry i am not able to understand this"]
    ]
    
]

def chat():
    chatbot = Chat(pairs,reflections)
    chatbot.converse()


# In[ ]:


chat()


# In[ ]:





# In[ ]:




