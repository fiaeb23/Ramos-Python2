#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Übung 3.01


# In[ ]:


def symbolen (variable):
    for i in variable:
        print (i * "x")

variable = [1,2,3]
symbolen(variable)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a)  ANTWORT
x
xx
xxx

b)
x
xx
x

c)
xxx
xx
x


# In[ ]:





# In[ ]:





# In[ ]:


# Übung 3.03


# In[6]:


test = [10,11,12]
test[1] = 15
test


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a) [10,11,12]
b) [10,15,12]  ANTWORT
c) [12,11,10]


# In[ ]:





# In[ ]:


# Übung 3.07


# In[8]:


def test2():
    string = 'hallo welt-test'
    print(string)
    
string = 'hallo welt' 
test2()
print(string)

welche ist die Antwort?
a)
hallo welt
hallo welt

b)
hallo welt
hallo welt-test

c)                 ANTWORT
hallo welt-test
hallo welt
# In[ ]:




