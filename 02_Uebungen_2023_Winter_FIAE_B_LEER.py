#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Übung 11


# In[43]:


liste = ['Apfel', 'Banane','Kiwi']
test = liste[0:1]
print(test)

welche ist die Antwort?
a) ['Apfel']
b) ['Banane']
c) ['Kiwi']
# In[ ]:





# In[ ]:


# Übung 12


# In[45]:


liste = ['Apfel', 'Banane','Kiwi']
test1 = liste[-1:]
print(test1)

welche ist die Antwort?
a) ['Apfel']
b) ['Banane']
c) ['Kiwi']
# In[ ]:





# In[ ]:


# Übung 13


# In[2]:


def x():
    return 2

x = 1+x()
print(x)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a) 2
b) 3
c) 4


# In[ ]:





# In[ ]:


# Übung 14


# In[6]:


def f(v):       
    v[0] = 2       
    print(v)   

a = [4, 5, 6]
f(a)

welche ist die Antwort?
a) [4, 5, 6]
b) [4, 2, 6]
c) [2, 5, 6]
# In[ ]:





# In[ ]:


# Übung 15


# In[8]:


def inkrementieren(a, b=1):       
    return a+b

print(inkrementieren(3,0))

welche ist die Antwort?
a) 3
b) 4
c) 5
# In[ ]:





# In[ ]:


# Übung 16


# In[10]:


def inkrementieren(a, b=1):       
    return a+b

print(inkrementieren(3))

welche ist die Antwort?
a) 31
b) 4
c) keine Antwort
# In[ ]:





# In[ ]:


# Übung 17


# In[55]:


def sterne():    
    for i in range(2):        
        print('*' * 5)
        
sterne()

welche ist die Antwort?
a) *****

b) *****
   *****

c)*****
  *****
  *****
# In[ ]:





# In[14]:


# Übung 18


# In[20]:


def sagen(a='hallo', b='tschüss'):       
    print(a + ' und ' + b)   

sagen(b='adeu', a='wie geht es')

welche ist die Antwort?
a) hallo und tschüss
b) wie geht es und adeu
c) adeu und wie geht es
# In[ ]:





# In[56]:


# Übung 19


# In[24]:


print ("HEMD ........................... 1")
print ("GÜRTEL ......................... 2")
print ("SCHUHE.......................... 3")

 
relation = {1:35, 2:10, 3:50}
 
code = 1
print ("Der preis ist: euros", relation[code])
menge = 3

preis = float(relation[code] * menge)-10
 
print ("Insgesamt: $", preis)

Wie viel ist der Preis insgesamt?
a) Insgesamt: $ 95.0
b) Insgesamt: $ 105.0
c) Insgesamt: $ 115.0
# In[ ]:





# In[2]:


# Übung 20


# In[26]:


p_dic = {'nombre':'Calico', 'edad':25}   
p_dic['edad'] = p_dic['edad'] + 1   
print(p_dic)

welche ist die Antwort?
a) {'nombre': 'Calico', 'edad': 24}
b) {'nombre': 'Calico', 'edad': 25}
c) {'nombre': 'Calico', 'edad': 26}
# In[ ]:




