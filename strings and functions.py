#!/usr/bin/env python
# coding: utf-8

# In[1]:


s=input("enter a string")
flag=0
for i in range (0,int(len(s)/2)):
    if s[i]==s[len(s)-i-1]:
        flag=1
if flag==1:
    print("string is palindrome")
else:
    print("string is not palindrome")


# In[2]:


s=input("enter string")
w=s.split()
print("words in even length")
for s1 in w:
    if(len(s1)%2==0):
        print(s1)


# In[3]:


s=input("eneter string")
def reverse(s):
    w=s.split()
    for s1 in w:
        for i in range(len(s1)-1,-1,-1):
            print(s[i],end=" ")
        print(" ",end=" ")
print(reverse(s))


# In[5]:


n=int(input("enter a number"))
def perfect(n):
    s=0
    for i in range(1,n):
        if (n%i)==0:
            s=s+i
            i+1
    if n==s:
        print("number is perfect")
    else:
        print("number is not perfect")
print(perfect(n))


# In[6]:


s=input("eneter string")
def reverse(s):
    w=s.split()
    for s1 in w:
        for i in range(len(s1)-1,-1,-1):
            print(s[i],end=" ")
        print(" ",end=" ")
print(reverse(s))


# In[7]:


s1= input("enter a string1")
s2= input("enter a string2")
a=set([])
for ch in s1:
    if ch in s2:
        a.add(ch)
print("number of match char=",len(a))


# In[8]:


def max(a,b,c):
    if(a>=b) and (a>=c):
        largest=a
    elif(b>=a) and (b>=c):
        largest=b
    else:
        largest=c
    return largest
print(max(12,34,45))


# In[9]:


s=input("enter a string")
i=int(input("enter position"))
s1=s[0:i]+s[i+1:]
print("after removing =",s1)


# In[10]:


s=input("enter a string")
w=s.split()
for s1 in w:
    for i in range(len(s1)-1,-1,-1):
        print(s1[i],end="")
  


# In[11]:


s=0
l=[1,2,3,4,5]
for i in l:
    s=s+i
    i+1
print("sum of list item =",s)


# In[12]:


s=input("enter a string")
n=len(s)
flag=0
if n%2:
    mid=n//2+1
else:
    mid=n//2
start=0
end=mid
while(start<mid and end<n):
    if (s[start]==s[end]):
        start=start+1
        end=end+1
    else:
        flag=1
        break
if flag==0:
    print("string is symmetrical ")
else:
    print("string is not symmetrical")


# In[13]:


n=int(input("enter a number"))
def test_prime(n):
    f=0
    if n==1:
        f=1
    elif n==2:
        f=0
    else:
        for i in range(2,n):
            if n%i==0:
                f=1
    if f==0:
        print("number is prime")
    else:
        print("number is not prime")
print(test_prime(n))


# In[14]:


def unique(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique([1,2,1,3,4,5,3,4]))


# In[15]:


s= input("enter a string")
a=set([])
vowels={'a','e','i','o','u'}
for ch in s:
    if ch in vowels:
        a.add(ch)
if len(a)==5:
    print(s,"is accepted")
else:
    print(s,"is not accepted")


# In[ ]:




