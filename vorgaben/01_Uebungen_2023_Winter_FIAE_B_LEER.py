#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Übung 1


# In[2]:


def test(a): 
    for i in range(a): 
        print('X'*2)
    
test(5)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a)
XX
XX
XX
XX
XX

b)
XXX
XXX
XXX
XXX
XXX

c)
X
X
X
X
X


# In[ ]:





# In[ ]:


# Übung 2


# In[4]:


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

c)
hallo welt-test
hallo welt
# In[ ]:





# In[ ]:


# Übung 3


# In[10]:


def frage(n1, n2 = 5):
    if (n1 < n2):
        print(n2, 'ist großer')
    elif(n2 < n1):
        print(n1, 'ist großer')
    else:
        print('sind gleich')
    
frage(5)

welche ist die Antwort?

a) 5 ist großer
b) sind gleich
# In[ ]:





# In[6]:


# Übung 4


# In[5]:


a = 'hallo'
b = 'welt'
print(a,'und',b)

welche ist die Antwort?
a) hallo und welt
b) welt und hallo
c) welt und welt
# In[ ]:





# In[8]:


# Übung 5


# In[7]:


def test3(c,d='test'):
    print(c,'und',d)

a = 'hallo'
b = 'welt'    
test3(a,b)
test3(a)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a) hallo und test
b) welt und test
c) hallo und welt


# In[ ]:





# In[10]:


# Übung 6


# In[9]:


a = 'hallo'
b = 'welt'
print(a + b)

welche ist die Antwort?
a) hallo
b) welt
c) hallowelt
# In[ ]:





# In[12]:


# Übung 7


# In[11]:


a = 'hallo'
b = 'welt'
c = a + b
print(c[:-1]) 

welche ist die Antwort?
a) hallow
b) hallowelt
c) hallowel
# In[ ]:





# In[ ]:


# Übung 8


# In[13]:


a = 'hallo'
b = 'welt'
c = a + b
print(c[-4:-1])
#von der -4 position bis -1 

welche ist die Antwort?
a) w
b) wel
c) welt
# In[ ]:





# In[15]:


# Übung 9


# In[14]:


def fragezeichen():
    return 20 

a = 30*fragezeichen()
print(a)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a) 6
b) 60
c) 600


# In[ ]:





# In[1]:


# Übung 10


# In[9]:


a = 2
b = 2

if (a != b):
    print(b)

welche ist die Antwort?
a) 2
b) error
c) keine Antwort