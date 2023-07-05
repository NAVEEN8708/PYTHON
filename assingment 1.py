#!/usr/bin/env python
# coding: utf-8

# In[1]:


#QUESTION1
a="my name is naveen"#string
b=[1,2,3] #list
c=2.390 #float
d=(1,2,34) #tuple


# In[2]:


#QUESTION 2
print(type(''))
print(type('[ds,ml,python]'))
print(type(['ds','ml','python']))
print(type(1.))


# In[3]:


#question3
print(5/2) #division operator
print(5%2) #modulo operator gives remainder
print(5//2) # gives quotient of division
print(5**2) # it means 5 raise to power 2


# In[4]:


#question4
l=[1,[2],"2.3","asd",{2},(2,3),{2,34},"python",2.444,[3,4]]
for i in range(0,len(l)):
    print(l[i],"   ",type(l[i]))


# In[5]:


#question5
a=int(input("enter no a="))
b=int(input("enter no b="))
if a%b ==0:
    print("a is purely divisible by b")
    c=0
    while a>=b:
        a=a//b
        c=c+1
    print("it can be divide by",c,"times")           
else:
    print("not purely divisble")

    
    


# In[6]:


#qestion6
l=[12,3,42,34,35,131,47,245,1,3,27,4,24,7,42,242,90,8,68,6,678,8,874,67,87]
for i in range(0,len(l)):
    if (l[i])%3==0:
        print(l[i],"   yes divisible by 3")
    else:
        print(l[i],"   not divisible by 3")


# In[7]:


#question 7
t=(12,45,67) #tuple data type.it is immutable data type means non changable
l=[12,34,56] #list data type.it is mutable data type means  changable that is l[1] can change
l[1]=2       #list second index is changed
print(l)


# In[ ]:




