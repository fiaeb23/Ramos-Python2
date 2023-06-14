#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Übung 4.16


# In[10]:


a = 'B'

if (a == "A" or a == "E" or a == "I" or a == "O" or a == "U"):
        print(a)

welche ist die Antwort?
a) B
b) error
c) keine Antwort
# In[ ]:





# In[28]:


# Übung 4.17


# In[6]:


def addieren(a):
    summe = 0
    for i in range (len(a)):  
           summe += a[i]
    return summe
         
test = [1,2,3]
print(addieren(test))

welche ist die Antwort?
a) 4
b) 6
c) 5
# In[ ]:





# In[ ]:


# Übung 4.18


# In[7]:


def generieren(a , b = 1): # a = 9, b = 3
    return a * b # 9 * 3

print(generieren(b = 3, a = 9))

welche ist die Antwort?
a) 3
b) 12
c) 27
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.19


# In[8]:


import random

for i in range (3):
    test = random.randint(1,3)
print('die Nummer ist',test)

welche ist die Antwort?
a) 1
b) 2
c) ein Wert zwischen 1 und 3
# In[ ]:





# In[ ]:


# Übung 4.20


# In[39]:


liste = ['Apfel', 'Banane','Kiwi']
for i in range(len(liste)):
    print(liste[i])

welche ist die Antwort?
a) 
Kiwi
Banane
Apfel

b) 
Apfel
Banane
Kiwi

c) 
Banane
Apfel
Kiwi
# In[ ]:





# In[ ]:


# Übung 4.21


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


# Übung 4.22


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


# Übung 4.23


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


# Übung 4.24


# In[11]:


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


# Übung 4.25


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


# Übung 4.26


# In[14]:


def inkrementieren(a=1, b=1):       
    return a+b

print(inkrementieren(1,2))

welche ist die Antwort?
a) 31
b) 4
c) keine Antwort
# In[ ]:





# In[ ]:


# Übung 4.27


# In[9]:


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


# Übung 4.28


# In[10]:


def sagen(a='hallo', b='tschüss'):  
    print(a,'und',b)

sagen(b='adeu', a='wie geht es')

welche ist die Antwort?
a) hallo und tschüss
b) wie geht es und adeu
c) adeu und wie geht es
# In[ ]:





# In[56]:


# Übung 4.29


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





# In[ ]:


# Übung 4.30


# In[26]:


p_dic = {'nombre':'Calico', 'edad':25}   
p_dic['edad'] = p_dic['edad'] + 1   
print(p_dic)

welche ist die Antwort?
a) {'nombre': 'Calico', 'edad': 24}
b) {'nombre': 'Calico', 'edad': 25}
c) {'nombre': 'Calico', 'edad': 26}
# In[ ]:





# In[ ]:


# Übung 4.31


# In[29]:


def keine_ahnung(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print (ANTWORT_1)
    elif n2 > n1 and n2 > n3:
        print (ANTWORT_2)
    elif n3 > n1 and n3 > n2:
        print (ANTWORT_3)
    else:
        print (ANTWORT_4)

keine_ahnung(3,4,2)

Was wäre eine passende Ergänzung als Antwort?

a)
ANTWORT_1 = n1, " ist die größte Zahl"
ANTWORT_2 = n2, " ist die größte Zahl"
ANTWORT_3 = n3, " ist die größte Zahl"
ANTWORT_4 = "sind gleich"

b)
ANTWORT_1 = n1, " ist die kleinste Zahl"
ANTWORT_2 = n2, " ist die kleinste Zahl"
ANTWORT_3 = n3, " ist die kleinste Zahl"
ANTWORT_4 = "sind gleich"

c)
ANTWORT_1 = "sind gleich"
ANTWORT_2 = "sind gleich"
ANTWORT_3 = "sind gleich"
ANTWORT_4 = "sind gleich"

# In[ ]:





# In[ ]:


# Übung 4.32


# In[31]:


def ungewissen (variable):
    cont = 0
    for i in variable:
        cont += 1
    return cont

ungewissen ([1,2,3,4])


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a) 2
b) 4
c) 5


# In[ ]:





# In[ ]:


# Übung 4.33


# In[35]:


def buchstabe (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return ('richtig')
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return ('richtig')
    else:
        return ('falsch')
    
buchstabe('E')

welche ist die Antwort?
a) 'richtig'
b) 'falsch'

# In[ ]:





# In[ ]:


# Übung 4.34


# In[37]:


def unbekannte (variable):
    operation = 0
    for i in variable:
        operation += i
    return operation

unbekannte([1,2,3])

welche ist die Antwort?
a) 4
b) 5
c) 6
# In[ ]:





# In[ ]:


# Übung 4.35


# In[39]:


def eine_Operation(n, z):
    print (n * z)

eine_Operation(2, 30)

welche ist die Antwort?
a) 2
b) 30
c) 60
# In[ ]:





# In[61]:


# Übung 4.36


# In[59]:


def symbolen (variable):
    for i in variable:
        print (i * "x")

variable = [1,2,3]
symbolen(variable)


# In[ ]:


get_ipython().set_next_input('welche ist die Antwort');get_ipython().run_line_magic('pinfo', 'Antwort')
a)
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





# In[3]:


# Übung 4.37


# In[ ]:


def frage(variable):
    var = 0
    for i in variable:
        if i > var:
            var = i
    return var

test = [1,2,3]
print(frage(test))

wie lautet das Ergebnis?
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.38

Für Ihr Projekt benötigen Sie Daten, die als Dictionaries-Variablen eingeben können.
Wählen Sie 2 Ausdrücke, die Sie dazu verwenden können:
a) leute ={'id_1':123, 'id_2':456, 'id_3':7 }
b) leute ={'id_1':'123', 'id_2':'456', 'id_3':'7' }
c) leute ={id_1:'123', id_2:'456', id_3:'7' }
d) leute ={id_1:123, id_2:456, id_3:7 }
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.39


# In[11]:


def sagen(a='hallo', b='tschüss'):       
    print(a + ' und ' + b)   

sagen()

Datentyp String: wie nennt sich die Operation: "a + ' und ' + b" ?

a) konkatenieren
b) addieren
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.40


# In[ ]:


def sagen(a='hallo', b='tschüss'):       
    test = a + ' und ' + b
    print(test[2:5])

sagen()

Datentyp Sring: wie nennt sich die Operation: test[2:5] ?
        
a) konkatenieren
b) addieren
c) slicen
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.41


# In[ ]:


liste = [5,6,7,8]

liste = liste[-3:2]
liste = liste[-1]
print(liste)

Was ist der erwartete Output des folgenden Codes?

a) 5
b) 6
c) 7
d) 8

# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.42

Ein Klassenkonstruktor...
(Wählen Sie 2 richtige Antworten aus):
    
a) Kann einen Wert zurückgeben
b) Kann nicht direkt innerhalb der Klasse aufgerufen werden
c) Wird bei der Vererbung von der Subklasse aufgerufen
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.43

Welche der folgenden Ausdrücke wird immer als wahr evaluiert?

a) len(random.sample([1,2,3],2)) > 2
b) random.choice([1,2,3]) > 0
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.44

Welchen Wert hat die Variable i nachdem die while-Schleife fertig abgearbeitet ist?
# In[ ]:


i=0
while i != 0:
    i=i-1
else:
    i=i+1
print(i)

a) 0
b) 1
c) 2
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.45

Was ist der erwartete Output des folgenden Codes?
# In[ ]:


a=3
if a >= 0:
    a+=1
else:
    a-=1
print(a)

a) 2
b) 3
c) 4
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.46


# In[ ]:


Angenommen, folgender Code wird fehlerfrei ausgeführt. 
a=[0]
b=a[:]
a[0]=1

get_ipython().set_next_input('Welche der folgenden Vergleiche sind RICHTIG');get_ipython().run_line_magic('pinfo', 'RICHTIG')
(Wählen Sie 2 richtige Antworten aus.)

a) len(a) == len(b)
b) a[0] -1 == b[0]
c) a[0] == b[0]
d) b[0] -1 == a[0]


# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.47

Betrachten Sie folgenden Code:
test = {'id_1':12, 'id_2':34}
if (BEDINGUNG):
    print('Key exists')

Mit welcher Bedingung lässt sich explizit überprüfen, ob ein bestimmter 
'key' in einem Dictionary namens "test" existiert?
(Wählen Sie 2 richtige Antworten aus)

a) 'id_1' in test
b) test['id_1'] != None
c) test.exists('id_1')
d) 'id_1' in test.keys()
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.48

Betrachten Sie folgenden Code:

def sterne():
    for i in range(5):
        print('*' * 3, end=" ")
        
sterne()
print('Hallo', end=" ")
sterne()Welche Ausgabe entspricht gleichzeitig dem Ergebnis von Code?

a) *** *** *** *** *** Hallo *** *** *** *** *** 
b) ** ** ** ** ** Hallo ** ** ** ** ** 
c) * * * * * Hallo * * * * * 
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.49


# In[ ]:


def unbekannt(wort_liste, n):
    for i in wort_liste:
        if len(i) > n:
            print (i)
            
liste = ['hola','hund', 'katze']
n = ???
unbekannt(liste, n)

Welcher Wert soll die Variable "n" haben, um das Wort 'katze' durch die Funktion "unbekannt" herauszubekommen?

a) 2
b) 3
c) 4
# In[ ]:





# In[ ]:





# In[ ]:


# Übung 4.50


# In[ ]:


def frage(liste):
    cont = 0
    for i in liste:
        if i > 20:
            cont += 1
    print (cont)
    
test = [1,2,40,50]
frage(test)

Welcher Wert werden Sie aus der Code herausbekommen und welche wäre die beste Beschreibung von dem Ergebnis?

a) 1 Wert kleiner als 20
b) 1 Wert größer als 20
c) 2 Werte kleiner als 20
d) 2 Werte größer als 20
# In[ ]:





# In[ ]:




