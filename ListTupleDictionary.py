#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={1:"om",2:"sai",3:"ram"}
print(d)
d[4]="sham"
print(d)


# In[2]:


s1={1,2,3,4}
s2={1,2,3,4}
if(s1.issubset(s2)):
    print("s1 is subset of s2")
else:
    print("s1 is not subset of s2s")


# In[3]:


s1={1,2,3,4,5}
print(s1)


# In[4]:


t=(1,2,3,'om',1.2,3)
print(t)


# In[5]:


t=(1,2,3,4,5,6)
print(t)
print(type(t))


# In[6]:


s1={1,2,3,4}
s2={3,4,5,6,7}
print("diff=",s1-s2)


# In[7]:


l1=[]
if len(l1)==0:
    print("list is empty")
else:
    print("list is not empty")


# In[8]:


d={1:"om",2:"sai",3:"ram"}
for i in d:
    print(i,end=" ")


# In[9]:


s={1,2,3,4}
print(s)
for i in s:
    print(i,end=" ")


# In[10]:


s1={1,2,3,4}
print(len(s1))


# In[11]:


t=[2,3,4,5]
print(len(t))


# In[12]:


num=[12,32,43,12,12]
def summ(num):
    sum=0
    for i in num:
        sum+=i
    return sum
print(summ(num))


# In[13]:


l=[1,2,3,4]
t=tuple(l)
print(t)


# In[14]:


s1={1,2,3,4}
print(max(s1))


# In[15]:


s=1
l=[1,2,3,4,5]
for i in l:
    s=s*i
    i+1
print("muliplication of list item =",s)


# In[16]:


l1=[1,2,2,3,3,2,4,2,5,6,6,7,8]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)


# In[17]:


t=[2,3,4,5,6]
print(t[1:])
print(t[1:3])


# In[18]:


d1={1:"om",2:"sai",3:"ram"}
s=sorted(d1.values())
print(s)
s2=sorted(d1.values(),reverse=True)
print("descending order list=",s2)


# In[19]:


t=(1,2,3,4)
if(5 in  t):
    print("elements exit")
else:
    print("elemetnt doesnt exist")


# In[20]:


t=(1,2,3,4)
if(5 in  t):
    print("elements exit")
else:
    print("elemetnt doesnt exist")


# In[21]:


n=int(input("enter limit"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)


# In[ ]:




