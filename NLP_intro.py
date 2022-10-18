#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


#compilando la regex
pattern = re.compile(r'bfoo\b')


# In[3]:


#texto de entrada
text = """bar foo bar foo barbarfoo foofoo foo bar"""


# In[4]:


# match nos devuelve None porque no hubo coincidencia al comienzo del texto
print(pattern.match(text))


# In[5]:


#match encuentra una coicidencia en el comienzo del texto
m = pattern.match('foo bar barbarfoo')
m


# In[6]:


#search nos devuelve la coincidencia en cualquier ubicación
s = pattern.search(text)
s


# In[7]:


# findall nos devuelve una lista con todas las coincidencias
f = pattern.findall(text)
f


# In[10]:


#finditer nos devuelve un iterador
fi = pattern.finditer(text)
fi


# In[12]:


# modificando el texto de entrada 


# In[13]:


# texto de entrada
becquer = """Podrá nublarse el sol eternamente;
Podrá secarse en un instante el marM
Podrá romperse el eje de la Tierra
como un débil cristal.
¡todo sucederá! Podrá la muerte
cubrirme con su fúnebre crespón;
Pero jamás en mí podrá´apagarse
la llama de tu amor."""


# In[14]:


pattern = re.compile(r'\W+')


# In[15]:


words = pattern.split(becquer)
words[:10]


# In[17]:


#utilizando la versión no compilada de un split
re.split(r'\n', becquer)


# In[18]:


pattern.split(becquer, 5)


# In[19]:


print(becquer)


# In[21]:


# limitando el número de reemplazos
podra = re.compile(r'\b(P|p)odrá\b')
puede = podra.sub('Puede', becquer)
print(puede)


# In[22]:


# limitando el número de reemplazos
puede = podra.sub('Puede', becquer, 2)
print(puede)


# In[23]:


# Banderas de compilación


# In[24]:


# Ejemplo de ignorecase
# cambiando 'Podrá' o 'podrá' por puede
podra = re.compile(r'podrá\b', re.I)
puede = podra.sub('Puede', becquer)
print(puede)


# In[ ]:




