#!/usr/bin/env python
# coding: utf-8

# ### AUFGABEN

# 1) Erstellen Sie eine Summe durch zwei Parameter mit Hilfe einer Methode

# In[ ]:


def add(x, y):
    get_ipython().run_line_magic('pinfo2', '')

a = add(2, 3)
print(a)


# In[ ]:





# In[ ]:





# 2) Definieren Sie eine Funktion "sendmail", um die Antwort zu bekommen:
# 
# von: person_1
# 
# zu: person_2

# In[ ]:


def sendmail(von, zu):
    get_ipython().run_line_magic('pinfo2', '')

sendmail('person_1','person_2')


# In[ ]:





# In[ ]:





# 3) Wie viel Mals darf man das Passwort nach dem unteren Code eingeben?

# In[ ]:


def ausprobieren(info, wiederholung=3):
    while wiederholung > 0:
        eingabe = input('{} ({}): '.format(info, wiederholung))
        if eingabe == 'geheimnis':
            return True
        wiederholung -= 1
    return False

print(ausprobieren("Passwort eingeben: ", 1))


# In[ ]:





# In[ ]:





# 4) welche Methode wird Python auswählen, um den Befehl "print" ausführen zu lassen?

# In[25]:


def add(x, y):
    return x*y

def add(x):
    return x+x

print(add(2))


# In[ ]:





# In[ ]:





# 5) Wenn Sie den Befehl "print" ausführen, bekommen Sie die richtige Ergebnisse?

# In[35]:


a = [2, 18]

def rechnen(numbers):
    total = 0
    for v in numbers:
        total += v
    return total, total / len(numbers)

x, y = rechnen(a)
print("Summe von a: {}  Durchschnitt von a: {}".format(y, x))


# In[ ]:





# In[ ]:





# 6) Wenn die Methode "aendern" ausgeführt wird, wie lautet 
# die Ausgabe "print(aendern(zahlen))" ?
# 
# a) [5,6]
# 
# b) [5,6,3]

# In[42]:


zahlen = [1, 2, 3]

def aendern(y):
    y = [5, 6]
    return y

print(aendern(zahlen))


# In[ ]:





# In[ ]:




