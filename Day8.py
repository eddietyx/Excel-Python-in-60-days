#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Day 8


# In[1]:


# bytes([source[, encoding[, errors]]]):字符串转换为字节类型
s = "apple"
bytes(s,encoding='utf-8')


# In[2]:


# str(object='')： 字符类型/数值类型转换为字符串类型
i = 100
str(i)


# In[3]:


# chr(i)：查看十进制整数对应的 ASCII 字符
chr(65)


# In[4]:


# ord(c): 查看某个 ASCII 字符对应的十进制数
ord('A')


# In[5]:


# dict()
dict(a='a',b='b')


# In[6]:


dict(zip(['a','b'],[1,2]))


# In[7]:


dict([('a',1),('b',2)])


# In[8]:


# int(x, base =10)，x 可能为字符串或数值，将 x 转换为一个整数。
int('12')


# In[9]:


int('12',16)


# In[11]:


# frozenset([iterable]):创建一个不可修改的冻结集合，一旦创建不允许增删元素。
s = frozenset([1,1,3,2,3])
s


# In[14]:


# list: list 函数还常用在，可迭代类型（Iterable）转化为列表
m = map(lambda i:str(i), [186,1243,3201])
l = list(m)
l


# In[15]:


list(map(lambda x: x%2==1, [1,3,2,4,1]))


# In[16]:


# range(stop)；range(start, stop[,step])
range(11) # 只有一个参数，默认初始值为 0，步长为 1


# In[17]:


range(0,10,1) #三个参数都提供，分别是开始、终止、步长值
# for i in range(0,10,1)


# In[18]:


# set([iterable]): 返回一个集合对象，并允许创建后再增加、删除元素。容器里不允许有重复元素，因此可对列表内的元素去重
a = [1,4,2,3,5,5,5]
set(a)


# In[19]:


# slice(stop)；slice(start, stop[, step]): 返回一个由 range(start, stop, step) 所指定索引集的 slice 对象
a = [1,4,2,3,1]
a[slice(0,5,2)] #等价于a[0:5:2]


# In[21]:


# tuple([iterable]): 创建一个不可修改的元组对象
t = tuple(range(10))
t


# In[22]:


# type(object)；type(name, bases, dict): 查看对象的类型的函数
type((1,2,3))


# In[25]:


# zip(*iterables): 创建一个迭代器，聚合每个可迭代对象的元素。
# 参数前带 *，意味着是可变序列参数，可传入 1 个，2 个或多个参数。
a = range(5)
b = list('abcde')
[str(y) + str(x) for x,y in zip(a,b)]


# In[27]:


# delattr(object, name)
# 删除对象的属性，在不需要某个或某些属性时
class Student():
    def __init__(self,id=None,name=None):
        self.id = id
        self.name = name

xiaoming = Student(1,'xiaoming')
delattr(xiaoming,'id')
hasattr(xiaoming,'id')


# In[ ]:


# dir([object])
# 不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时返回参数的属性、方法列表。


# In[28]:


# getattr(object, name[, default]): 获取对象的属性
getattr(xiaoming,'name')


# In[29]:


# isinstance(object, classinfo): 判断 object 是否为类 classinfo 的实例，若是，返回 true。
isinstance(xiaoming,Student)


# In[33]:


# issubclass(class, classinfo): 如果 class 是 classinfo 类的子类，返回 True
issubclass(Student,object), issubclass(object,Student)


# In[34]:


# super([type[, object-or-type]])
# 返回一个代理对象，它会将方法调用委托给 type 的父类或兄弟类。
# 子类的 add 方法，一部分直接调用父类 add，再有一部分个性的行为
class Parent():
    def __init__(self,x):
        self.v = x
    
    def add(self,x):
        return self.v + x

class Son(Parent):
    def add(self,y):
        r = super().add(y) #直接调用父类的add方法
        print(r) #子类的add与父类相比，能实现对结果的打印功能
        
Son(1).add(2)


# In[35]:


# callable(object): 判断对象是否可被调用，能被调用的对象就是一个 callable 对象，比如函数 str、int 等都是可被调用的
callable(str)


# In[36]:


# not callable:
xiaoming = Student('001','xiaoming')
callable(xiaoming)


# In[38]:


# instead: 必须要重写 Student 类上 __call__ 方法
class Student1():
    def __init__(self,id=None,name=None):
        self.id = id
        self.name = name
    def __call__(self):
        print('I can be called')
        print(f'my name is {self.name}')
        
t = Student1('001','xiaoming')
t()


# In[ ]:




