#!/usr/bin/env python
# coding: utf-8

# In[12]:


name = input ("Enter File: ")
handle = open(name)

counts= dict()
for line in handle: 
    words= line.split()
    for word in words:
        counts[word]= counts.get(word,0) +1
        
#print(counts)
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword =word
        bigcount = count
        
print ("The Most Repeated word in your text is: '",bigword,"'", "it occurs:",bigcount, "times in your text")


# In[ ]:




