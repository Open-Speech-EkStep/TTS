#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


with open('../cmu_indic_pan_amp/etc/txt.done.data', encoding='utf-8') as file:
    text = file.readlines()
    print(text)


# In[9]:


cleaned_text = []
lines = []

for local_text in text:
    local_text = local_text.strip()
    local_text = local_text.split(' ')
    local_text = local_text[1:-1]
    filename = local_text[0]
    local_text = local_text[1:]
    content = " ".join(local_text)[1:-1]
    one_line = filename + '|' + content + '|' + content
    lines.append(one_line)


# In[12]:


with open('metadata.csv', mode='w+', encoding='utf-8') as file:
    file.writelines("\n".join(lines))


# In[ ]:




