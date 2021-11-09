#!/usr/bin/env python
# coding: utf-8

# In[2]:


if True:
    print("line1")
    print("line2")
else:
    print("line3")
print("line4")
    


# In[3]:


if 1==1:
    print("condition is true")
    
else:
    print("condition is not true")
print("code outside if else statement")
    


# In[4]:


if 1==2:
    print("condition is true")
    
else:
    print("condition is not true")
print("code outside if else statement")


# In[5]:


# when we dont want the condition to statement, we will use [pass]
# no here pass is not working for the conditional statements, it only works for loops line for and while
if 1==2:
    print("condition is true")
    
else:
    pass
    print("condition is not true")
print("code outside if else statement")


# In[6]:


age=22
salary=20000
if age>=20:
    print("you are eligible for cc")
elif salary>=25000:
    print("you are eligible for cc")
else:
    print("you are not eligible")


# In[12]:


age = 20
salary = 20000
if age >= 20:
    if age >= 20 and salary >= 20000:
        print("you are eligiuble for credit card")
    else:
        print("you are not eligiuble for credit card")
elif salary > 25000 and age < 20:
    print("you salary is eligible but your age is not eligible for credit card")
else:
    print("you are not eligiuble for credit card")


# In[15]:


# program for elif
marks = 90
if marks >= 90 and marks < 100:
    print('a')
elif marks >= 80 and marks < 90:
    print('b')
elif marks >= 70 and marks < 80:
    print('c')
elif marks >= 60 and marks < 70:
    print('d')
else:
    print('fail')


# In[16]:


# FOR LOOP
for i in "kapil":
    print(i)


# In[17]:


for i in "kapil":
    print(i,end="")


# In[18]:


# if we want give the space between in string "kapil"
for i in "kapil":
    print(i,end=" ")


# In[19]:


for i in "kapil":
    print(i,end=",")


# In[22]:


for i in "kapil":
    print(i+'edyoda')
    


# In[23]:


stair = 0
stairs = ["stair1","stair2","stair3"]
for i in stairs:
    stair = stair + 1
    print(stair)


# In[24]:


stair = 0
stairs = ["stair1","stair2","stair3"]
for i in stairs:
    stair = stair + 1
print(stair)


# In[25]:


for i in 1:
    print(i)


# In[26]:


for i in str(1):
    print(i)


# In[37]:


for i in tuple("abs"):
    print(i)


# In[41]:


for i in str(1000):
    print(i,end="")


# In[1]:


bin(10)


# In[2]:


bool("false")


# In[3]:


bool()


# In[4]:


a=[1,2,3]
print(a)
print([1,2,3])


# In[6]:


my_list=[0,1,2,3,4,5]
print(my_list[3:7])


# In[8]:


for i in range(1,28):
    print(i)


# In[11]:


i=input("")
l=["a","e","i","o","u"]
if i in l:
    print("it is vowel")
else:
    print("it is consonent")


# In[2]:



a=["a","e","i","o","u",'A']
i=input()
if i in a:
    print('vowel')
else:
    print('consonant')


# In[3]:



a=['A','E','I']
i=input()
if i.lower() in a:
    print('vowel')
else:
    print('consonant')


# In[4]:



a=['A','E','I']
i=input()
if i.lower() in a:
    print('vowel')
else:
    print('consonant')


# In[5]:



a=['A','E','I']
i=input()
if i.lower() in a:
    print('vowel')
else:
    print('consonant')


# In[6]:



a=['A','E','I']
i=input()
if i.upper() in a:
    print('vowel')
else:
    print('consonant')


# In[7]:



a=['A','E','I']
i=input()
if i.upper() in a:
    print('vowel')
else:
    print('consonant')


# In[2]:


my_str="naveen kumar"
print(my_str[5::-1])


# In[5]:


my_str="naveen kumar"
slice_index=slice(1,6)
print(slice_index)
my_str[slice_index]


# In[6]:


a=[1,2,3,4,5]
len(a)


# In[11]:


result=0
for i in [1,2,3,45]:
    result+=1
    print(result)
    
print(result)


# In[13]:


result=0
for i in [1,2,3,4]:
    result+=i
    print(result)
    
print(result)


# In[22]:


a="naveen"
r=range(1,10)
print(r[0])
print(r[3])
print(r[5])
print(r)
slice_variable=slice(1,5)
print(a[slice_variable])
for i in r:
    print(i)
    


# In[23]:


for i in range(0,3):
    print('inside range loop')
    for s in 'str':
        print('inside string loop')
        for l in [1,2,3]:
            print('inside list loop')


# In[26]:


for i in range(0,2):
    print('inside range loop')
    for s in [1,2]:
        print('inside string loop')
        for l in [1,2,3]:
            print('inside list loop')


# In[30]:


for i in range(5):
    for j in range(i+1):
        print('@',end='')
    print()


# In[31]:


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


# In[36]:


for i in range(0,5):
    for j in range(i+1):
        print("*",end="")
    print()


# In[37]:


for i in range(1,6):
    print(i)


# In[40]:


for i in range(0,5):
    for j in range(i+1):
        print('#',end="")
    print()


# In[44]:


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()


# In[ ]:




