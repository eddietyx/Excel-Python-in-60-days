#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Day 7: mathematic calculations


# In[3]:


# max(iterable, *[,key,default]): variables after * could only be keywork argument, but not positional argument
a = [1,2,3,4,5,1]
max(a, key = lambda x: a.count(x))
# max(iterable) = max(iterable,*,key) = max(iterable,*,default) = max(iterable,*,key,default)


# In[6]:


# sum(iterable, /, start = 0): argument before / could only be positional argument
a = [1,2,3,4,5,1]
sum(a) # sum = 16 
sum(a,2) # 表示求和的初始值为2 instead of default = 0


# In[7]:


# pow(x,y,z=None,/)
# x to the power of y, and return the remainder divided by z ~ (x^y / z)
pow(3,2,4)


# In[8]:


# round(number[,ndigits])
# ndigits = 小数点后几位
round(10.0222222,3)


# In[9]:


# divmod(a,b) 分别取商和余数
divmod(10,3)


# In[10]:


# complex([real[,imag]]) to create a complex number
complex(1,2)


# In[11]:


# hash(object) return the hash value of an object
hash('xiaoming')


# In[12]:


# id(object) return the id of the object
id('xiaoming')


# In[14]:


# all(iterable) return True if all elements are real, else False
all([1,0,3,2]), all([1,2,3])


# In[17]:


# any(iterable) return True if one of elements is true
any([0,0,1]), any([0,0,0,[]])


# In[18]:


# bin(int) 十进制转化二进制
bin(10)


# In[19]:


# oct(x) 十进制转化八进制
oct(10)


# In[20]:


# hex(x) 十进制转化十六进制
hex(16)

