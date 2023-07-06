#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Hausaufgabe 1


# In[2]:


def frage(n1,n2): # (n1 = 5, n2 = 8)
    if (n1 < n2):
        print(n2, 'ist größer')  # n2 = 8
    elif(n2 < n1):
        print(n1, 'ist größer')
    else:
        print('sind gleich')
        
frage(5,8)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a) 5 ist größer
b) 8 ist größer
c) sind gleich


# In[ ]:





# In[42]:


# Hausaufgabe 2


# In[1]:


def frage(n1,n2,n3):  # n1 = 1, n2 = 2, n3 = 3
    if (n1 < n2) and (n2 < n3) :  #1 < 2 and 2 < 3   # JA and JA = JA
    #if (n1 < n2) and (n2 < n3) :   #2 < 1 and 1 < 3   # NEIN and JA = NEIN
        print(n1, 'ist kleiner')
    elif(n2 < n1) and (n2 < n3) :
        print(n1, 'ist großer')
    else:
        print('sind gleich')
        
frage(1,2,3)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a) 3 ist größer
b) 2 ist größer
c) 1 ist kleiner


# In[ ]:





# In[ ]:


# Hausaufgabe 3


# In[3]:


#       0  1  2
test = [10,11,12]
test[1] = 15
test


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a) [10,11,12]
b) [10,15,12]
c) [12,11,10]


# In[ ]:





# In[ ]:


# Hausaufgabe 4


# In[5]:


def lager(a): # a = [10,11,12]
    a[0]=15   # a = [15,11,12]
    print(a)

test = [10,11,12]  # 
lager(test)
print(test)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a)
[10, 11, 12]
[15, 11, 12]

b)
[15, 11, 12]
[10, 11, 12]

c)
[15, 11, 12]
[15, 11, 12]


# In[ ]:





# In[6]:


# Hausaufgabe 5


# In[47]:


for i in range(5):
    print('X')


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a)
XX
XX
XX
XX
# XX

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




