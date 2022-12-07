#!/usr/bin/env python
# coding: utf-8

# In[1]:


height=float(input("enter height"))
base=float(input("enter base"))
area=(height*base)/2
print("area of traingle=",area)


# In[1]:


height=float(input("enter height"))
base=float(input("enter base"))
area=(height*base)/2
print("area of traingle=",area)


# In[1]:


height=float(input("enter height"))
base=float(input("enter base"))
area=(height*base)/2
print("area of traingle=",area)


# In[ ]:





# In[ ]:





# In[2]:


n=int(input("enter a number"))
s=0
n1=n
while n>0:
    d=n%10
    s=s+(d*d*d)
    n=n/10
if s==n1:
    print("number is armstrong")
else:
    print("number is not armstrong")


# In[3]:


n=int(input("enter a number"))
if n>=0:
    if n==0:
        print("number is zero")
    elif n>0:
        print("number is positive")
else:
    print("number is negative")


# In[4]:


n=int(input("enter a number"))
flag=0
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            flag=1
            break
if flag==0:
    print("number is prime")
else:
    print("number is not prime")


# In[5]:


n=int(input("enter a number"))
f=1
if n<0:
    print("factorial doesnt exist")
elif n==0:
    print("facrorial of 0 is one")
else:
    for i in range(1,n+1):
        f=f*i
    print("factorial=",f)


# In[6]:


n=int(input("enter a number"))
if (n%2)==0:
    print("number is even")
else:
    print("number is odd")


# In[7]:


import random
n=random.random()
print("random number=",n)


# In[8]:


x=5
y=10
temp=x
x=y
y=temp
print("value of x=",x)
print("value of y=",y)


# In[ ]:




