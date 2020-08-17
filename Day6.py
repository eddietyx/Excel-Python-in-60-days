#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Python 60 days - Day 6: examples and usage in dict and sets

# 1. Update: insert key-values
d = {'a':1, 'b':2}
d.update({'c':3, 'd':4, 'e':5})
# same ways: d.update([('c',3), ('d',4)], e = 5)
# tuples in a list or equation format
d


# In[4]:


# 2. setdefault : 仅当dict中某个key不存在时才会插入，否则不会插入（避免修改已有key-valiue）
d = {'a':1, 'b':2}
r = d.setdefault('c',3) # r:3
r,d


# In[5]:


r = d.setdefault('c',33)
r,d # r:3, 'c':3 has already existed and setdefault will not change the key-value of c


# In[7]:


x = d.setdefault('c',33)
x,d # x:3, by changing the variable, the value set of dict will not be changed


# In[10]:


# sort by key
def sort_by_key(d):
    return sorted(d.items(), key = lambda x: x[0])

sort_by_key(d)


# In[13]:


# sort by value
def sort_by_value(d):
    return sorted(d.items(), key = lambda x: x[1]) # items as x, and use x[1] as key to be sorted and return d.items
sort_by_value(d)


# In[14]:


# return max key
# main idea: use keys function to get all keys and get the max of them and return
def max_key(d):
    if len(d) == 0:
        return []
    max_key = max(d.keys())
    return (max_key, d[max_key])

max_key({'a':1, 'd':4, 'b':2})


# In[15]:


# return max value
# main idea: for the max value, there might be more than one key with the same max value
def max_val(d):
    if len(d) == 0:
        return []
    max_val = max(d.values())
    return [(key, max_val) for key in d if d[key] == max_val]

max_val({'a':1, 'c':3, 'e':5, 'd':4, 'ee':5})


# In[16]:


# set
s = {1,3,5,7}


# In[18]:


# use set to seperate string without duplication
set('python'), set('ppyy')


# In[19]:


# 单字符串
def single(string):
    return len(set(string)) == len(string) # use the fact that set will delete duplication

# o is the duplication in function one
single('love_python'), single('python')


# In[20]:


# find the longer set
def longer(s1,s2):
    return max(s1,s2, key = lambda x: len(x))

longer({1,2,3}, {1,2,3,'a','b'})


# In[22]:


longer({1,2,3}, {1,2,3,3,3}) # since set does not allow duplication, then it will automatically delete duplication before compare


# In[25]:


# find the value that is repeated the most
# find the value that is repeated the most in two sets, and return the single value by default
def max_overlap(lst1, lst2):
    overlap = set(lst1).intersection(lst2) # find all the intersected value without duplication
    # ox is a list of tuples
    ox = [(x,min(lst1.count(x), lst2.count(x))) for x in overlap] # find the min of count of the same value in both lst1 and lst2 which could be regarded as the times it shows in both sets
    return max(ox, key = lambda x: x[1]) # compared by the count of each value

max_overlap([1,1,1,2,2,2,2,3,3], [2,2,4,4,3,2,2,1])


# In[27]:


# find the keys of the top n values in a dict
# use built-in function nlargest in heapq
from heapq import nlargest

def top_n_key(n,d):
    return nlargest(n, d, key = lambda x: d[x])

top_n_key(3, {'a':1, 'd':4, 'c':3, 'e':5, 'f':6, 'z':26, 'b':2})
# the result is sorted by value


# In[32]:


# one key, multiple values

# regular way
def order_by_key(lst):
    d = {}
    for k, v in lst:
        if k not in d:
            d[k] = [] # create an empty key in d
        d[k].append(v) # append a new value to the d.values for the same key
    return d

lst = [(1,'a'),(1,'o'),(1,'x'),(3,'b'),(3,'z'),(2,'t')] # only list of tuples is accepted here
order_by_key(lst)
    


# In[37]:


# more efficient way
# by using defaultdict in collections which could create the key-value set by default
from collections import defaultdict
# return defaultdict(list, {}) where first argument must be callable, which is list here
d = defaultdict(list)
for k,v in lst:
    d[k].append(v) # no need to check and create empty key 
    
d


# In[39]:


# merge dicts logically
# without changing the value in the original dicts
dict1 = {'x':1, 'y':2}
dict2 = {'y':3, 'z':4}
merged = {**dict1, **dict2}
merged


# In[40]:


merged['x'] = 10
merged, dict1
# the value of x in dict1 will not be changed since the merged dict is created seperately from dict1 and dict2


# In[41]:


# change the value of the original dict by using ChainMap in collections
# it has automatically created a list of these dicts internally
from collections import ChainMap
merged1 = ChainMap(dict1, dict2)
merged1


# In[42]:


merged1['x'] = 10
merged1, dict1


# In[45]:


merged1['y'] = 100
merged1, dict1, dict2
# 如果在不同dicts中存在相同的keys，那么在修改赋值的时候只会修改一次，by default 对第一个进行修改


# In[ ]:




