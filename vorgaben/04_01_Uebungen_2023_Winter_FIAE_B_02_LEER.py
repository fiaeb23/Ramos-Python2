#!/usr/bin/env python
# coding: utf-8

# In[5]:


##### Übung 4.01


# In[17]:


zahlen = {
    "id_1": "123",
    "id_2": "456",
    "id_3": "189"
}

Lassen Sie durch die Methode „items()“ über eine For-Schleife die Schlüssel und die Objekte des Dictionarys „zahlen“ zeigen:
# In[ ]:





# In[3]:


##### Übung 4.02


# In[ ]:


buchstaben = ['a','b','c','d','e','f','g','h','i','j']


# In[ ]:


get_ipython().set_next_input('Welcher Ausdruck ist wahr');get_ipython().run_line_magic('pinfo', 'wahr')

a) buchstaben[:] == buchstaben[::]
b) buchstaben[:] != buchstaben[::]
c) len(buchstaben[:]) == len(buchstaben[::])
d) len(buchstaben[:]) != len(buchstaben[::])


# In[ ]:





# In[ ]:





# In[ ]:


##### Übung 4.03


# In[ ]:


Betrachten Sie folgenden Code:


# In[ ]:


numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
numbers[::2] = [0,0,0,0,0,0]
print(numbers)


# In[ ]:


get_ipython().set_next_input('Was ist die erwartete Ausgabe');get_ipython().run_line_magic('pinfo', 'Ausgabe')
a) [1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0]
b) [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11,12]
c) [0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12]
d) [0, 0, 0, 0, 0, 0]


# In[ ]:





# In[ ]:





# In[4]:


##### Übung 4.04


# In[7]:


def run():
    print("legen wir los")


# Lassen Sie die Funktion "run" ausführen

# In[ ]:





# In[ ]:





# In[6]:


##### Übung 4.05


# Holen Sie die Funktion „laufen“ über die Python-Datei „module.py“ ein, um die Funktion „laufen“ auszuführen.

# In[ ]:





# In[ ]:





# In[8]:


##### Übung 4.06


# Rufen Sie die Funktionen a, b, _c aus der Python-Datei "variablen" auf. Wie lautet die Antwort?
# 

# In[ ]:





# In[ ]:





# In[10]:


##### Übung 4.07

Rufen Sie alle Funktionen aus der Python-Datei "variablen.py" auf. Wie lautet die Antwort?
# In[ ]:


__all__ = ['a','b', '_c', 'd']

def a():
	return "in a"

b = "Wert von b"

def _c():
	return "in _c"

def d():
	return "in d"


# In[ ]:




