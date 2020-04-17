

# Python

## Review Session

### 1. Python Basics

- data type/structures
- Module/functions
- Exception  handling
- Class & objects (inheritance)
  - instance variable, global variable, private variable
- iteration & generators
- function map
  - f = lambda x:x[0]
  - def g(f, x): \n  return f(x)+1
  - g(lambda x:x[0], [1,2,3])

### 2. Text Processing

- data I/O
- Regex (same complexity with midterm)
- Nature Language Processing NLTK
  - not anything too deep. but like concoice, frequency, etc
  - not based on documentation, but based on fundemental python basics

### 3. Multi-dimensional Data

- Manipulation: NumPy. 
  - difference between numpy array and python list.
  - regular index, fancy index, mask, like t = s[s>0] (create a copy)
    - A[[1,3]]
  - create view, copy
    - List. c=b[:] is copy, c=b is view (dictionary works the same)
    - np.array. d=a[:] and d=a are all view. but d=a.copy is a copy.
  - Reshape, modify and find data type (dtype)
- Visualization: Matplotlib, NetworkX
  - Edge list, and adjacency matrix
  - Digraph, the matrix will not be symmetric. 
- imaging
  - Modify a given part of numpy, within the context of image.
  - Greyscale(2D or 3D, depends)/color image
- Pandas
  - Series
  - Dataframe
    - how load csv, excel
    - how specify the index of table
    - how to filter out the subset of data based on requirement, group
    - how to filter based on value of specific column

### 4. GUI

- TKinter
  - how set up tkinter from scratch
  - how to draw shape, button based on event
  - complexity similar to exercise
- Like container
- Inheritance of frame. Use its init.
- difference between tk.frame and tk.toplevel blabla is not important.

## Tips

- `print char,	` #加逗号不换行，而是用空格间隔！
- 效率：基本上，when you only need to perform a single function call, map > list comprehension > for loop
- print help(xxx) 可以调取使用说明

### 运行

starting the interpreter is `python -c command [arg] ...`, which executes the statement(s) in *command*, analogous to the shell’s [`-c`](https://docs.python.org/2/using/cmdline.html#cmdoption-c) option.

### Scope

python的for和while等，出了范围并不会删变量（非局域变量），而是保留变量最后的值

### Passing in Arguments

When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the `argv` variable in the `sys` module. You can access this list by executing `import sys`. 

```python
import sys
knightstour(int(sys.argv[1]))
```

同一目录下可以import进其他的py文件（不带py后缀）

```python
import mystuff as ms
```

### Module

`python -m module [arg]` ...

- dir(): 查看这个module的子功能

```python
dir(math)
```

#### random

```python
import random as rand
rand.random() #0-1
rand.randint(1,6) #int in 1~6

from random import * #this is bad
random()

from Option import *

```

#### <u>time</u>

```python
import time
begin = time.clock() #record start time
#your code goes here
end = time.clock() # record end time"
print end - begin #calculate difference (elapsed time)
```

### environment

To declare an encoding other than the default one, a special comment line should be added as the *first* line of the file. The syntax is as follows:

```
# -*- coding: encoding -*-
```

where *encoding* is one of the valid [`codecs`](https://docs.python.org/2/library/codecs.html#module-codecs) supported by Python.



## 数据类型

### number

#### int & float

自动识别

#### calculator

The interpreter acts as a simple calculator: you can type an expression at it and it will write the value.

### String

- They can be enclosed in single quotes (`'...'`) or double quotes (`"..."`) with the same result [2](https://docs.python.org/2/tutorial/introduction.html#id4).  `\` can be used to escape quotes.

- 换行输入：`'''xxx'''`, xxx可以换行而不影响。

- without print, \n is included in the output

- 引号里放引号：

  ```python
  a2 = "here's" # one solution
  a2 = 'here\'s'
  ```

#### print

- translate escaped and special characters：print()

```python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print '"Isn\'t," they said.'
"Isn't," they said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print, \n is included in the output
'First line.\nSecond line.'
>>> print s  # with print, \n produces a new line
First line.
Second line.
```

- 不translate escape：print r "xxx"

  - 3.*: print(r "xxx")

  ```
  >>> print r'C:\some\name'  # note the r before the quote
  C:\some\name
  ```

- print不换行

- ```python
  print x, end=" "  # python 3.x, Appends a space instead of a newline
  print x,	#python 2
  ```
```
  
- print多行： using triple-quotes: `"""..."""` or `'''...'''`. End of lines are automatically included in the string, but it’s possible to prevent this by adding a `\` at the end of the line.

​```python
print """\	#表示这里不自动换行
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
```

- Strings can be concatenated (glued together) with the `+` operator, and repeated with `*`:

- ```python
  >>> 3 * 'un' + 'ium'
  'unununium'
  ```

- Two or more *string **literals*** (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.(not with variables or expressions)

```python
>>> 'Py' 'thon'
'Python'
```

#### format

```python
print("xxx%sxx%d" % (str,num))

>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
 
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
 
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
```



#### input

```python
>>> x = int(raw_input("Please enter an integer: "))
Please enter an integer: 42
  
  s = "you pushed me %d times"%self.push_count
```



#### Slicing

```python
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

- However, out of range slice indexes are handled gracefully when used for slicing:

```python
>>> word[4:42]
'on'
>>> word[42:]
''
```

#### immutable

- Python strings cannot be changed — they are [immutable](https://docs.python.org/2/glossary.html#term-immutable). Therefore, assigning to an indexed position in the string results in an error

- ```python
  >>> word[0] = 'J'
    ...
  TypeError: 'str' object does not support item assignment
  >>> word[2:] = 'py'
    ...
  TypeError: 'str' object does not support item assignment
  ```

#### len(s): built in func.

### Lists

#### 内置函数

```python
list1 = []
s = len(list1)
list1.insert(0, w)
l = list("abc") #['a','b','c']
#concatention
squares + [36, 49, 64, 81, 100]	#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#以下都不return anything，而是直接改变list1
list1.append(w)
list1.remove(w) #the first occurrance of w
list1.pop(1) #remove the element in position 1
list1.sort()
list1.reverse()	#不return任何东西(None)，只改变list1
list2 = list1[:]	#create a copy of list
list2 = list1 #list2变了，list1也跟着变! (只有list, dictionary是这样）
```

#### List Comprehension

```python
#带if语句
a = [i**2 for i in range(5) if i%2==0] #0, 4, 16
# _ 表示空variable
b = [0 for _ in range(5)] #we can use _ if we don't need a variable
#两个for，后面的for在前面的里面
[i+j for i in range(2) for j in range(4)] #[0, 1, 2, 3, 1, 2, 3, 4]
#list里套list，基本variable是里面的list
[[i+j for i in range(2)] for j in range(4)]	#[[0, 1], [1, 2], [2, 3], [3, 4]]
```

```python
#practice
#[[1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12]]:
[[i*j for i in range(1,4)] for j in range(1,5)]
#[0, 0, 0, 0, 1, 2, 0, 2, 4, 0, 3, 6, 0, 4, 8, 0, 5, 10]:
[i*j for i in range(6) for j in range(3)]
```

### Tuple

#### 命名

```python
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5) #nested
t[0] = 88888 #error! tuples are immutable
singleton =('hello',)
empty = ()
```

#### 赋值

```python
#Fibonacci series:
>>> a, b = 0, 1
>>> while b < 1000:
...     print b,
...     a, b = b, a+b
```



### Set

- A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

#### 命名

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> fruit = set(basket)               # create a set without duplicates
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>>empty = set() #不能用empty = {}，这个出来的是空dictionary
```

#### 逻辑运算

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
>>> a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                              # letters in both a and b
set(['a', 'c'])
>>> a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])
```

### Dictionary

#### 命名

```python
{x: x**2 for x in (2, 4, 6)} {2:4, 4:16, 6:36}
d4 = {1:{3:4, 5:6}} #dictionary里可以包含dic
d4[3] = 2
```

#### 遍历

```python
for key, value in d.items():
for value in d.values():
for key in d.keys():
for key in d:
```

#### 内置函数

```python
dict.items()
dict.has_key(key)
dict.clear()
cmp(dict1, dict2)
dict.get(key) #default=None
dict.update(dict2) #替换成dict2
dict.values()	#a list of all values in dict, 重复的也会打出来
```

## Function

### docstring

The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or *docstring*. (More about docstrings can be found in the section [Documentation Strings](https://docs.python.org/2/tutorial/controlflow.html#tut-docstrings).) There are tools which use docstrings to automatically produce online or printed documentation, or to let the user interactively browse through code; it’s good practice to include docstrings in code that you write, so make a habit of it.

### <u>检查数据类型</u>

```python
isinstance(x, (int, float)) #检查x是不是(int, float)
```

### 内置函数

- `math.sqrt()` 算平方根

- `quadratic(a, b, c)`，接收3个参数，返回一元二次方程 ax2+bx+c=0*a**x*2+*b**x*+*c*=0 的两个解

- `in` 判断一个element是否在一个list或tuple里 （`if ok in ('y', 'ye', 'yes')`)

- filter

  ```python
  seq = [1,2,5,1,2,5,4,3]
  filter(lambda x: x%2, seq)
  ----
  [1, 5, 1, 5, 3]
  ```

- map

  map() expects a function to be passed in. This is where **lambda** routinely appears.

  ```python
  map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
  [1, 4, 9, 16, 25]
  map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
  [3, 7, 11, 15, 19]
  
  #pass in 多个参数：
  x1 = [1,2,3,4,5]
  x2 = [2,3,4,5,6]
  map(lambda t,s: t+s, x1, x2) #[3, 5, 7, 9, 11]
  ```

- reduce

  ```python
  >>> reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
  15
  ```

- enumerate

  ```python
  2
  l = ['tic', 'tac', 'toe']
  for i, v in enumerate(l):
      print i, v
  ---
  0 tic
  1 tac
  2 toe
  ```

- zip

  ```python
  >>> for q, a in zip(questions, answers):
  ...     print 'What is your {0}?  It is {1}.'.format(q, a)
  ```

- reversed()

  ```python
  # try to accomplish this using slicing
  l = range(1,10,2)
  for i in reversed(l):
      print i
  ----
  9 7 5 3 1
  ```

- **iteritems**

  ```python
  month_name = {1: 'Jan', 2: 'Feb', 3:'Mar'} 
  for k, v in month_name.iteritems():
      print k, v
  ----
  1 Jan
  2 Feb
  3 Mar
  ```

### 注意事项

function里放function，有先后顺序，先def，之后才能调用！

```python
#关于function的reference
def h(d,e):
    d = 10	#不会改变
    e[0] = 5	#改变
    e = [1,2]	#不会改变
b = 2
a = [1,2,3]
h(b,a)
print b #2
print a #[5,2,3]
```



#### 参数位置

The default values are evaluated at the point of function definition in the *defining* scope, so that

```python
i = 5
def f(arg=i):
    print arg
i = 6
f() 	#print 5
```

#### 默认参数

**Important warning:** The default value is evaluated **only once**. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

```python
def f(a, L=[]):
    L.append(a)
    return L

print f(1)	#1
print f(2)	#1,2
print f(3)	#1,2,3

#只改变特定参数：
def my_fun(a=10, b=20):
    print a,b
my_fun(b=30)
```

### 参数

#### 可变参数

- 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个`*`号。在函数内部，参数`numbers`接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

```python
>>> calc(1, 2)
5
>>> calc()
0
```

Python允许你在list或tuple前面加一个`*`号，把list或tuple的元素变成可变参数传进去：

```python
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```

#### 关键字参数

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

函数`person`除了必选参数`name`和`age`外，还接受关键字参数`kw`。在调用该函数时，可以只传入必选参数：

```python
>>> person('Michael', 30)
name: Michael age: 30 other: {}
```

也可以传入任意个数的关键字参数：

```python
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

#### lamda

Small anonymous functions can be created with the [`lambda`](https://docs.python.org/2/reference/expressions.html#lambda) keyword. This function returns the sum of its two arguments: `lambda a, b: a+b`. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43

f = lambda x, y : x + y
f(1,1) #2

```

## Catch Error

- IOError
  If the file cannot be opened.
- ImportError
  If python cannot find the module
- ValueError
  Raised when a built-in operation or function receives an argument that has the
  right type but an inappropriate value
- KeyboardInterrupt
  Raised when the user hits the interrupt key (normally Control-C or Delete)
- EOFError
  Raised when one of the built-in functions (raw_input()) hits an
  end-of-file condition (EOF) without reading any data
- NameError
  Raised when a local or global name is not found. 或者比如"int(abc)",如果没用定义abc=一个数，则NameError
- IndexError
- ZeroDivisionError
- TypeError 数据类型错误

### Try & except,  as

如果except错误的error种类，则无效。

```python
#利用except规避错误
while True:
    try: 
        s = float(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."

#记录下error信息
def divide(x,y):
    try: 
        print x/y
    except (ZeroDivisionError, TypeError) as ze:
         print "there's an error!", ze
divide(1,2)
divide(1,0)
divide("1",0)
```

### Raise

The [`raise`](https://docs.python.org/2/reference/simple_stmts.html#raise) statement allows the programmer to force a specified exception to occur. For example:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

## Class

### \__name__

- 在外面直接运行这个py文件时，\__name__是main. 被import时，name是modole name

The only thing that’s unusual here is how the *name* variable works. It takes on a different value depending on whether it appears in the script you chose to run or in an imported module. In the script you chose to run, _*name_* takes on the value _*main_*. In an imported module, _name_ is the filename of the module. If this was not clear, please go back and/or do some tests of your own to understand its behavior.

The purpose of the `if _name_ == "_main_"` idiom is to enable certain code to run (often test code) when the user choses to run the file as a script but to prevent that same code from running if the file is imported as a module by another script.

- When you run a Python module with

```python
python fibo.py <arguments>
```

- the code in the module will be executed, just as if you imported it, but with the `__name__` set to `"__main__"`. That means that by adding this code at the end of your module:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

- you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:

```python
$ python fibo.py 50
1 1 2 3 5 8 13 21 34
```

- If the module is imported, the code is not run:

```python
>>> import fibo
```

- This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).

### class variable

- shared by all instances of class
- 在init外面定义的变量，默认为class variable，默认为public variable, 可在外面改变
- 每一个instance创建时可以选择改变整个class的值
- 如果直接给一个object的class variable赋值则只会改变这个object的值，而不会影响其他的。del它之后它变回class的值

```python
d = DblClass(3, 'data')
d.count = 5
print d.count	#这时是自己的值
print DblClass.count	#不改变class variable
```

### Instance variable

- The concept of __“instance variable”__ is the same in C++/Java, but note that they are declared within a method (member function)! You do not list all your instance variables outside the methods like you do in C++/Java; you just initialize them inside the methods.

- The __self__ variable is similar to the __this__ pointer/reference in C++/Java, but you have to include it as the first parameter in the definition of every method. Also, while this was not always necessary for referring to instance variables in C++/Java, in Python, you always have to use self in order to refer to an instance variable.
- The __"object"__ has two meanings: the most basic kind of thing, and any instance of 

正确的每个object独有的变量定义方法，在init里，而不是在function外面：

(也可以在别的func里面，且public，但不规范）

```python
def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
```

### private variable

在init里面，前面加__，变成private variable，class外面无法access

```python
class MyClass(object):
	a = 1	#class variable
    def __init__(self, x = 2, y = 3):
        MyClass.a = x	#不用在init外面声明，也会作为class variable，但不建议
        self.b = y	#instance variable
        self.__c = 10	#private variable
   
    def get__c(self):	#accessor
        return self.__c
     
    def set__c(self, x):	#manipulator
        self.__c = x
```

- 在外面给一个object的private variable赋值不会报错，而会新建一个新的instance来存值，且不影响真正的private variable

```python
o1 = MyClass()
o1.__c = 11
print o1.__c	#11, actually o1._MyClass__c
print o1.get__c()	#10
del o1.__c
o1.set__c(12)
print o1.get__c()	#12
```

### Built-in attributes

- C.\__doc__ #return docile
- C.\__bases__ #return parent class
- C.\__dict__ #return 所有信息

### Magic Methods

http://minhhh.github.io/posts/a-guide-to-pythons-magic-methods

### Tips

- 可以用dir(o1) 来获取一个object的所有方法和属性！也可以dir()任何对象比如list，来看可用的操作！

## <u>Iterator & Generator</u>

### Iterable

- List, Tuple, Set, Dictionary, etc.

### <u>Iterator</u>

an iterator is any object that defines a suitable __next__ method. When an iterator object’s __next__ method is invoked, the method should return the next element of some collection – whatever that may mean. How the __next__ method is written defines the order in which the elements of a collection are iterated over in a for loop.

#### \__iter__

Your collection appoints an iterator by defining an \__iter\__ method that returns an instance of an iterator object.

If the collection has its own next method, the collection’s \__iter\__ method can return self; the container will serve as its own iterator. 

### Iterator and Container are NOT the same object

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ReverseIterator(self)
    
class ReverseIterator:
    def __init__(self, reverseObject):
        self.index = len(reverseObject.data)
        self.r = reverseObject	#储存并传递参数
        
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.r.data[self.index]
```

### Iterator and Container are the same object

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):	#如果没有这个, TypeError: iteration over non-sequence
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

### StopIteration

for loop terminates when it gets this exception

### <u>Generator</u>

#### Yield

Inside the for loop when the execution reaches the yield statement, the value of data[index] is returned and the generator state is suspended. During the second next call, the generator resumes from the index at which it stopped earlier and increases this index by one. It continues with the for loop and comes to the yield statement again.

**yield** basically replaces the return statement of a function but rather provides a result to its caller without destroying local variables. Thus, in the next iteration, it can work on this local variable value again. So unlike a normal function that you have seen before, where on each call it starts with new set of variables - a generator will resume the execution where it was left off.

```python
def __iter__(self):
    return self.generator()
  
def generator(self):
    yield self.a
    yield self.b
    yield self.c
```



### Generator Expression

The generator expressions are the generator equivalent of a list comprehension, but with parentheses instead of square brackets. Just like a list comprehension returns a list, a generator expression will return a generator.

```python
squares = (x * x for x in range(1,10))
print(type(squares))	#<type 'generator'>
print(list(squares))	#[1,4,9,16,...]

#in function
def every_other(data):
    for index in range(0,len(data),2):
        yield data[index]
        
for char in every_other("supercalifragilisticexpialidocious"):
    print char,
```

#### With Lambda

```python
every_other2 = lambda data: (char for char in data[::2])
for char in every_other2("supercalifragilisticexpialidocious"):
    print char,	#不换行，而是用空格间隔！
#s p r a i r g l s i e p a i o i u 
every_other3 = lambda data: (data[index] for index in xrange(0,len(data),2)) # range would work, too
for char in every_other3("supercalifragilisticexpialidocious"):
    print char,
```

### enumerate(sequence, start=0)

Return an enumerate object. *sequence* must be a sequence, an [iterator](https://docs.python.org/2/glossary.html#term-iterator), or some other object which supports iteration. The `next()` method of the iterator returned by [`enumerate()`](https://docs.python.org/2/library/functions.html#enumerate) returns a tuple containing a count (from *start* which defaults to 0) and the values obtained from iterating over *sequence*:

```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

## Inheritance

子类init不会自动init父类。在子类里面，只有call了super(Child, self).\__init__()才会获得父类的variable。但父类的function子类和子类的object随时可以调用。

```python
class ClassA(object):	# (object) 必备！否则old style class，cannot use super
    static_var = 1
    
    def __init__(self):
        print "Initializing A"
        self.instance_var = 2 
        self.my_method()	#当B super(ClassB,self).__init__()时，actually call的是B的版本
        
    # this is new --
    def my_method(self):
        print "Do Something"
    # -- this was new
    
class ClassB(ClassA):
    def __init__(self):
        print "Initializing B"
        super(ClassB,self).__init__() 
        
    def my_method(self):
        print "Do Something Else"
        
    def my_super_method(self):
        super(ClassB,self).my_method()	# call parent's function. 注意括号里是子类class名字！
def main():
    
    b = ClassB()
    print "b.static_var =",b.static_var
    print "b.instance_var =",b.instance_var	#如果没有(object)：b does not have an instance_var because the superclass initializer doesn’t run automatically when we create an instance of the subclass
    b.my_method() # Do Something Else
    b.my_super_method() #Do Something
        
if __name__ == "__main__":
    main()
```

- Calling self's super:

```python
class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()	#when calling self, actually calls parent function
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

#PARENT altered()
#CHILD, BEFORE PARENT altered()
#PARENT altered()
#CHILD, AFTER PARENT altered()
```

#### Class Composition

call functions in another class. 一个class里initialize另一个class的object，然后在function里call相关的functions。

#### General guidelines:

- Avoid multiple inheritance at all costs.
- Use composition to package up code into modules that are used in many different unrelated places and situations.
- Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept.

## Read & Write

### Mode

| `'r'` | open for reading (default)                                   |
| ----- | ------------------------------------------------------------ |
| `'w'` | open for writing, truncating the file first                  |
| `'x'` | open for exclusive creation, failing if the file already exists |
| `'a'` | open for writing, appending to the end of the file if it exists |
| `'b'` | binary mode                                                  |
| `'t'` | text mode (default)                                          |
| `'+'` | open for updating (reading and writing)                      |
| `r+`  | read and write                                               |

- r+：可读可写，若文件不存在，报错
- w+: 可读可写，若文件不存在，创建

### Syntax

```python
f = open ("filename", "w")
f.write("hello")
f.close()	#如果不close，改动可能无法添加上去

f = open("filename","r").read() #把文件内容直接读进去，不用close

with open ("filename", "a") as f:	#don't need to close
	f.write("hello")

with open("myfile.txt","r") as f:
    x = f.read()	#可赋值
    print x
```

### helpful Functions

```python
f.closed #return True or False
f.readline() #return the next line in f
```

### OS

```python
#create dir
if not os.path.exists('audio'):
    os.makedirs('audio')
file = 'audio/' + url.split('/')[-1]
if not os.path.exists(file):
```



## CSV

### Syntax

```python
import CSV
#Reader:
with open(‘some.csv’, ‘rb’) as f:
	reader = csv.reader(f)
	for row in reader:
		print row

#一项项的处理：
d = []
with open("simpledata.csv", "r") as f:
    reader = csv.reader(f)
    row_num = 0
    for row in reader:
        if row_num == 0:
            d.append(row)
        else:
            d.append([row[0].upper(),row[1]])	#一个个单词是被放在list里面的
        row_num += 1
print d

#Writer:
with open("simpledata2.csv", "w") as f:
    writer = csv.writer(f)
    for row in d:
        writer.writerow(row)	#写一行：writer.writerow
```

### Functions

- csv.reader
- csv.writer
- csv.register_dialect
- csv.unregister_dialect
- csv.get_dialect
- csv.list_dialects
- csv.field_size_limit

## Regular Expressions

### Functions

#### match

- 匹配string从开头开始。

  ```python
  prog = re.compile(r'abc*')
  print prog.match('abcdddd').group()	#abcdddd
  #以下的大写表示非这个
  \d 数字
  \s space
  \w [a-zA-Z0-9_]
  \b 单词开始或结尾
  ```

#### search

- takes as input a pattern and a string, and returns an object (of a class that is specific to the __re__ module) that contains the first substring matching the pattern, together with its location in the string. We can call the former using the __group()__ attribute, and the latter using the __start()__ and __end()__ attributes. 
  - Group()返回匹配上的值。
- group()` allows us to group the pattern, using parentheses, such that we can call different parts of it. 

```python
re.search(r'abc','abcd').group()	#abc
re.search(r'abc','abcd').start()	#0
re.search(r'abc','abcd').end()	#3

re.search(r'((a)b)c','abcd').group(1)	#ab, nested从外到内
re.search(r'((a)b)c','abcd').group(2)	#a
re.search(r'([a-z])\d\1','g3g h4h').group()	#g3g, 只返回第一个
```

#### findall

-  Returns a list containing all substrings that match the pattern, without information about their location.
- 返回从头到尾每一个匹配上的substring作为element，且对每一个element从外到内依次返回每一个catch的group

```python
re.findall(r'(([a-z])\d\2)','g3g h4h')	#[('g3g', 'g'), ('h4h', 'h')]
```

#### finditer

大概等同于多个search，返回callable-iterator。

```python
mails2 = re.finditer(r'[0-9a-zA-Z]+[\[| ]?(@|at|AT)[\]| ]?[0-9a-zA-Z]+([\[| ]?(\.|dot|DOT)[\]| ]?[a-z0-9A-Z]+){0,}', page)
res = []
for i in mails2:
    res.append(i.group())
```

#### sub

```python
#replace法
s='aba'
s=s.replace('a','c',2)	#把s里面的前2个a变成c

#sub法
str = re.sub(r'( at | AT |\[at\]|\[AT\])',r'@', str)	#把str里面的pattern1，全部换成pattern2(literal meaning)
```

### Lookforwards & lookbackwards & 不catch

```python
#不catch (?:xxx)
mails = re.findall(r'[0-9a-zA-Z]+(?:@| at | AT |\[at\]|\[AT\])[0-9a-zA-Z]+(?:(?:\.| dot | DOT |\[dot\]|\[DOT\])[a-z0-9A-Z]+){0,}', page)	#使用(?:xxx),否则return的list里还有被catch的小groups

#Lookahead (?=xxx)
s='1.86 5.30 8.54 13.75'
re.findall(r'\d+(?=[.])',s) #在[]里，"."被当作字面含义
re.findall(r'\d+(?=\.)',s) #和上面相等
#negative lookahead (?!xxx)

#Lookbehind (?<=xxx)
re.findall(r'(?<=[a-z] )[A-Z][a-z]+',s) #空格不用加转义
#匹配每个前面是小字母+空格，且大写开头的单词。
#negative lookbehind (?<!xxx)
```

## urllib2

读取网页源码：

```python
#python2
import urllib2
url = "http://www.math.ucla.edu/~hangjie/contact"
page=urllib2.urlopen(url).read()

#python3
import urllib
page=urllib.request.urlopen(url).read()

#download file
try:
  urllib.request.urlretrieve(url, filename = file)
  except Exception as e:
    print("Error occurred when downloading file, error message:",e)
```

## Localhost

```python
python -m SimpleHTTPServer port

> python -m SimpleHTTPServer 8099
Serving HTTP on 0.0.0.0 port 8099 ...
127.0.0.1 - - [24/Oct/2017 11:07:56] "GET / HTTP/1.1" 200 -
1.2. 基于python3
python3 -m http.server port

> python3 -m http.server 8099
Serving HTTP on 0.0.0.0 port 8099 (http://0.0.0.0:8099/) ...
127.0.0.1 - - [24/Oct/2017 11:05:06] "GET
```

### Data Cleaning

```python
times=open('marathon.txt', 'r').read()
Lrows=re.split(r'\n',times)	#每一行变成一个element

L=[re.split(r'\s+|:',i) for i in Lrows] #以多个space或者：来分词

#改变数据类型
for i in L:
    for j in [1,2]:
        i[j] = int(i[j])
```

## Matplotlib

### syntax

```python
%matplotlib inline	#draw chart inline
import matplotlib.pyplot as plt

#x轴和y轴分别放点
plt.plot([0,1,2,3],[5,9,3,2])
plt.show()	#显示图标

#坐标范围：xleft,xright,ydown,yup
plt.axis([-1,4,0,10])

#同时放多个
plt.plot(x, np.sin(x), 'ro', x, 2*np.cos(x), 'b')

#ogrid，生成纵轴array和横轴array
import matplotlib.pyplot as plt
x,y=np.ogrid[0:1:500j,0:1:500j]	#nj表示n个间隔
#z=x*x+y*y
z = np.sin(3.0*np.pi*x)*np.cos(3.0*np.pi*y)
plt.imshow(z)
plt.colorbar()	#加bar
plt.show()

import matplotlib.image as mpimg 
img=mpimg.imread('kitty-cat.jpg') 
plt.imshow(img)
plt.show()
```

### style

**linestyle**

matlab style

- b- (default): blue line

- : 方点，--间断横，-. 横点横点，

- ```
  '-'solid line style
  '--'dashed line style
  '-.'dash-dot line style
  ':'dotted line style
  '.'point marker
  ','pixel marker
  'o'circle marker
  'v'triangle_down marker
  '^'triangle_up marker
  '<'triangle_left marker
  '>'triangle_right marker
  '1'tri_down marker
  '2'tri_up marker
  '3'tri_left marker
  '4'tri_right marker
  's'square marker
  'p'pentagon marker
  '*'star marker
  'h'hexagon1 marker
  'H'hexagon2 marker
  '+'plus marker
  'x'x marker
  'D'diamond marker
  'd'thin_diamond marker
  '|'vline marker
  '_'hline marker
  The following color abbreviations are supported:    
  character
  color
  ‘b’blue
  ‘g’green
  ‘r’red
  ‘c’cyan
  ‘m’magenta
  ‘y’yellow
  ‘k’black
  ‘w’white
  ```

**tag**

```python
plt.title('My plot')
plt.xlabel('horizontal')
plt.ylabel('vertical')
```

## Numpy

### 考点

More coding things. Less Multiple choices. load image into numpy, modify a little bit, create mask, etc. Not responsible for the blur formula and any mathematical things.

### Syntax

```python
import numpy as np
#arange, <type 'numpy.ndarray'>
x = np.arange(20) #0,1, ..., 19
t = np.arange(0., 5., 0.2)	#0, 0.2, ..., 4.8, 不一定加点，(0,5,0.2)

#array
x = np.array([[1,2],[2,3],[3,4]])

#linespace 从a到b，一共c个数,包括a和c
x = np.linspace(0,1,10)	#0, 0.111, 0.222, ..., 0.888889, 1.0
y = np.linspace( 0, 2, 9 ) #[0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]
#显示属性
print x.shape #几乘几的矩阵,tuple形式，可以用index来access每个维度
print x.ndim #几维坐标，等于x.shape有多少个数
```

### Functions

**常用函数**

```python
y = np.sin(x)	#处理整个list
np.zeros((3,4))	#全为0
np.ones( (2,3,4), dtype=np.int16 )  #全为1(int)
np.empty( (2,3) ) #任意值, dtype default is float64
img2 = np.full((400, 400,3), 255) #全是255的三维矩阵
#access
print img[50,50] #等同于img[50][50]
```

**reshape**

General rule: when specifying the shape of an array, columns is always last. Rows is second to last. "Pages" is third to last. And so on.

Caution: for efficiency, many NumPy operations avoid copying data. They just give you different *views* of the underlying data.	#reshape只改变表现形式，是reference，而不是copy。

```python
#reshape
x = np.arange(24)
y = x.reshape((24,1)) #24行，1列
y = x.reshape((4,6))	#4行，6列
z = x.reshape((2,3,-1))	#2 pages, 3 rows, as many columns as needed to preserve the number of elements
x[0]=10	#y,z也跟着边

print z[1,2,0]	#第二页的[2,0]
#遍历矩阵
for rownum in range(img.shape[0]):
	for colnum in range(img.shape[1]):
    greyImg[rownum][colnum] = average(img[rownum][colnum])
```

**Slicing**

Slicing works the same way as it did with lists. It creates a **view**(reference）

```python
#1D
y = x[1:8:2]	#[1 3 5 7]

#2D
y = x[100:200, 150:550]	#前面是行，后面是列
y = x[:,-1] #最后一列全部行，且变成1D array
```

**Copy**

```python
x = np.array([[1,2],[2,3],[3,4]])
y = x.copy()
y[0] = 100	#y变，x不变
```

**View**

```python
img3[250:650, 100:500] = img2.view()
img2 = ... 	#不会改变img3，因为img3本身不是view，而上一行只是生成了一个view用来给3赋值而已
```

### Mask

**copy & view**

```python
# fancy indexing creates a copy
x = np.arange(5)
y = x[[0,2]]	#x的第0和第2个
y[0] = 3	#不改变x

# slicing creates a view
x = np.arange(5)
y = x[0:2]
y[0] = 3	#改变x
```

**boolean mask**

自己的mask只能给自己用。出来的都是一维数组

```python
x = np.arange(10)
mask = x <= 6	#含np array的判断句
print mask	#[ True  True  True  True  True  True  True False False False]
print x[mask]	#[0 1 2 3 4 5 6]

#logic operation
mask1 = x <= 6
mask2 = x >= 3
mask3 = np.logical_and(mask1, mask2)	#[False False False  True  True  True  True False False False]
mask4 = np.logical_xor(mask1, mask2) #[ True  True  True False False False False  True  True  True]
mask=(x>30)&(x<70)&(30<y)&(y<70)
im[mask]=[1,1,1]
```

**Boolean masks create a *copy* of the data.**

```python
y = x[mask]
y[:] = 0	#只会把y全变成0，不会改变x
#x=[0 1 2 3 4 5 6 7 8 9]
#y=[0 0 0 0 0 0 0]
```

**fancy indexing: index array**

```python
x = np.arange(24).reshape((4,-1))	#4*6矩阵
y = np.arange(x.shape[1])	#利用x.shape[1]=6

#permutaion
i = np.random.permutation(y)	#随机打乱y的element,只会打乱第一维
print i
print x[:,i]	#根据i的排序来排列每一行

#generating
mult = np.array([[[1.0/3**2]*3]*3]*2)
"""[[[0.11111111 0.11111111 0.11111111]
  [0.11111111 0.11111111 0.11111111]
  [0.11111111 0.11111111 0.11111111]]

 [[0.11111111 0.11111111 0.11111111]
  [0.11111111 0.11111111 0.11111111]
  [0.11111111 0.11111111 0.11111111]]]
"""
im=[[[0,0,1]]*100]*100 
```

### *Linear Algebra

```python
a = np.array([[1.0, 2.0], [3.0, 4.0]])
a.transpose()
np.linalg.inv(a)
u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
j = np.array([[0.0, -1.0], [1.0, 0.0]])
j @ j        # matrix product
np.trace(u)  # trace, 2
y = np.array([[5.], [7.]])
np.linalg.solve(a, y)
np.linalg.eig(j)
```

### Operations

```python
a=np.array([[1,2],[3,4]])
b=np.array([[1.0/4.0,1.0/4.0],
            [1.0/4.0,1.0/4.0]])
a*b	#乘一一对应的的entries
sum(a)	#[4,6] ,对应的vector相加
np.sum(a)	#每个entries加起来
```

### Image preprocess

```python
#create a copy to process so that the original one doesn't change
greyImg = img.copy()

#convert datatype
img=mpimg.imread('kitty-cat.jpg') 
print img.dtype #uint8
img = img/255.0 #Convert to 64-bit floating point.

#access one color channel
plt.imshow(img[:,:,0],cmap='gray')  #red color channel

greyImg = img.copy()
for rownum in range(img.shape[0]):
    for colnum in range(img.shape[1]):
        greyImg[rownum][colnum] = average(img[rownum][colnum])
#“多维中的一个维度（比如有3个数）=一个数” 会把所有数都变成它
img[:]=1 会把所有数都变成1
#np.repeat拓维，向深度重复，一共3层
greyImg = np.repeat(greyImg[:, :, np.newaxis], 3, axis=2) #向深度重复，一共3层，axis表示数组维度（？）
```

### Blur

#### Gaussian Blur

```python
sigma = 1
k = 5
filter=np.array([[0]*k]*k,dtype='float')
for x in range(k):
    for y in range(k):
        filter[x,y]=np.exp(-((x-(k-1)*0.5)**2+(y-(k-1)*0.5)**2)/(2.0*sigma**2))
filter_sum=np.sum(filter)
filter=filter/filter_sum
```

### Edge Detection

```python
vertical_filter=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
horizontal_filter=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
```

## Tkinter

### syntax

```python
import Tkinter as Tk
root = Tk.Tk()
w = Tk.Canvas(root, width=500, height=500)
w.pack()
def func(event):	#must have one argument
  	w.create_xxx(...., fill="red")
w.bind("<Button-1>", func)
root.mainloop()
```

### 画图

```python
w.create_rectangle(event.x,event.y, event.x+20, event.y+20, fill="blue")
w.create_oval(event.x-15, event.y-15, event.x+15, event.y+15, fill="yellow")
w.create_polygon(event.x, event.y, 300, 400, 250, 230, fill="red")#至少3个点
self.canvas.create_arc(event.x, event.y, event.x+100, event.y+100, start=0, extent=270, fill='red')
self.canvas.create_text(100,100,text='hello!')
```

### 组件

```python
#button
def hit_me():
  ...
b = tk.Button(window, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

#在外面改一个组件的属性：
b['state'] = tk.DISABLED  #禁用
self.push_counter['text'] = "you pushed me %d times"%self.push_count
self.parent.button['state'] = tk.NORMAL #so now you have the MainScreen instance available as self.parent
self.parent.newWindow.destroy() #close window
  
#Toplevel
self.newWindow = tk.Toplevel(self)	#区别于root。把自己整个pass in
self.parent.newWindow.destroy() #close window
```

### <u>Class</u>

```python
class RectangleGUI:
    def __init__(self, master):
       self.master = master
       self.canvas = Tk.Canvas(master, width=500, height=500)
       self.canvas.pack()
       self.canvas.bind("<Button-1>", self.rectangle)	#!!!
    def rectangle(self,ev):	#must have the argument
       self.canvas.create_rectangle(ev.x, ev.y, ev.x+20, ev.y+20, fill="blue")

if __name__ == "__main__":
    root = Tk.Tk()
    gui=RectangleGUI(root)
    root.mainloop()
```

## Pandas

### Basics

#### Declare

```python
lsd = pd.read_table('lsd.txt','\t')	#return a dataframe
cs = pd.read_table('chopstick2_rcb.dat','\s+')

#用dict可以生成
df3 = pd.DataFrame({1:[1,2,3,4],'a':['A','B','C','D']})
df_test = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))	#index默认从0开始，integer
print df_test

df = pd.read_excel('data.xlsx', 'Worksheet', index_col=0) #index_col指定第0列为index
#用list
nan = float("nan")
table = [[1, 2],[nan,nan],[5,6],[nan, nan],[9,10]]
df = pd.DataFrame(table, columns = ["A","B"])

numbers = [i for i in range(21)]
df = pd.DataFrame(numbers, index = dates, columns = ["A"])
```

**Series**

- the__ Series__ object shows its index column, a list of integers by default, to the left of the actual data.

```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64(默认)
```

**date_range**

```python
dates = pd.date_range('20191121', periods=6)
"""DatetimeIndex(['2019-11-21', '2019-11-22', '2019-11-23', '2019-11-24','2019-11-25', '2019-11-26'], dtype='datetime64[ns]', freq='D') """

t=time()	#the number of seconds since January 1, 1970
dt = pd.to_datetime(t, utc = False, unit = "s")
#添加时区：
dt3 = pd.to_datetime(t, utc = True, unit = "s")
dt4 = dt3.tz_convert("US/Pacific")

dates = pd.date_range('20130101', '20130106', freq = "6H")
df = df.asfreq("9H", method = "pad")	#数据根据原数据图表📈修改
```

**np.random.rand(6,4)** 

- generates an object representing a two dimensional (six rows, four columns) array of random numbers between zero and one. 

#### Access

```python
#display(df)	#显示表格
#获取列
df.First
df["First"]

#获取行
df[3:7]	#从0开始，不包括最后
df["A1002":"A1005"]	#包括最后

#loc，用名字 (faster than indexing)
df.loc["A1002"]
df.loc["A1002":"A1005",["First","Last"]] # :和[]同理，“”表示的都包括最后

#iloc，用位置，不包括最后
df.iloc[1:5,[1,2]]	#注意后面包括2！
df.iloc[[1,4]]	#第1和4行

```

#### Plot

```python
plt.plot(lsd['drug'],lsd['math'],'o')	

type1 = cs['type']==1  
good = cs['eff'] >= 27
plt.xticks(np.arange(6)+1/2,['Type1','Type2','Type3','Type4','Type5','Type6']) 
plt.bar(np.arange(6),[len(cs[type1 & good]),
                      len(cs[type2 & good]),
                      len(cs[type3 & good]), 
                      len(cs[type4 & good]), 
                      len(cs[type5 & good]), 
                      len(cs[type6 & good])], 
        barwidth, color='r', label='Good')
plt.bar(np.arange(6)+barwidth,[len(cs[type1 & fair]),
                               len(cs[type2 & fair]),
                               len(cs[type3 & fair]), 
                               len(cs[type4 & fair]), 
                               len(cs[type5 & fair]), 
                               len(cs[type6 & fair])], 
        barwidth, color='b', label='fair')
```

### **Dataframe**

- index是key，获取数据的关键键。

### **Viewing**

```python
df.head()
df.tail()
df.index
df.columns
df.values
df.discribe #count, unique, top, freq
df.T 	#transpose
df.dtypes	#return每一列的data type
df.to_numpy()
```

### <u>Sort</u>

```python
df.sort_index(axis=0, ascending=True)	#axis：0按照行名排序；1按照列名排序
df.sort_values(by = "First")	#记得等号！
```

### Mask

```python
type1 = cs['type']==1 
good = cs['eff'] >= 27
plt.bar(np.arange(6),[len(cs[type1 & good]),
                      len(cs[type2 & good]),
                      len(cs[type3 & good]), 
                      len(cs[type4 & good]), 
                      len(cs[type5 & good]), 
                      len(cs[type6 & good])], 
        	barwidth, color='r', label='Good')

df["M" <= df.First]

df[df.First.isin(["Meredith","Summer"])]
df[df.First.isin(["Meredith","Summer"]) & (df.Phone >= "3")]	#用&来表示逻辑
df[df.First.isin(["Meredith","Summer"])].loc[:,"Phone"]

```

###Modify & Remove
```python
df.First[df.First < "B"] = "Unicorn"
y = df[1:]
y = df["A1002":]
y = df[df.index != "A1001"]

df = df[pd.notnull(df.A)] #去掉A中nan的行
df = df.set_index("A") #改变index

df["B"] = df.A %2	#加列
gb = df.groupby("B")
gb.aggregate(sum)
```

### 保存

```python
df.to_excel('data2.xlsx', sheet_name='Worksheet')
#sheet_name : str, int, list, or None, default 0
```

## NetworkX

#### 创建graph

```python
import matplotlib.pyplot as plt
import networkx as nx

G_mat = np.array([[0,1],[1,0]])
G = nx.Graph(G_mat)

G2 = nx.DiGraph()

W = nx.stochastic_graph(G, weight='weight')
```

#### 修改graph

```python
G2.add_node('A')
G2.add_nodes_from(['B','C','D']
G2.add_edge('A','B')
e = (2, 3)
G.add_edge(*e)
G.add_edges_from([(1, 2), (1, 3)])
G.remove_node(2)
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
```

#### 查看graph

```python
nx.draw(G,with_labels=True)
G.number_of_nodes()
list(G.nodes)
list(G.adj[1])
G.degree(2)

pr = nx.pagerank(G, alpha=0.85) # the default damping parameter alpha = 0.85
nx.draw(G,with_labels=True)
plt.show()
print(W['A'])	#{'C': {'weight': 0.5}, 'B': {'weight': 0.5}}
```



## SqLite3

```python
#To Database
conn = sqlite3.connect(database)
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS %s (File text, Content text)'%table)
conn.commit()
# df.to_sql('Res1', conn, if_exists='replace', index=False)
for row in range(df.shape[0]):
    cmd = "INSERT INTO {} (File,Content) VALUES ('{}','{}')".format(table, df["File"][row], df["Content"][row])
    c.execute(cmd)
    # print(df["File"][row], df["Content"][row])
conn.commit()
c.execute("SELECT * FROM %s"%table)
for row in c.fetchall():
    print(row)
```



## NLTK

### Basic Operation

```python
import nltk
from nltk.book import *
# Searching Text
text1.concordance("food")
# To find other words that appear in a similar range of contexts
text1.similar("food")
#出现位置标点
text1.dispersion_plot(["food", "time", "live", "here"])
# to get frequency distribution of some text频率表
fdist1=FreqDist(text1)
print(fdist1.most_common(5))
fdist1.plot(30, cumulative=False)

tokens = text.split()	#标点留在单词后面
tokens = nltk.word_tokenize(text)	#不保留标点符号
d = nltk.FreqDist(tokens)
lexical_diversity = float(len(d))/len(tokens) 

p = nltk.PorterStemmer()#去时态。类似dictionary指向普通时态
print p.stem("running")
```

### Search

```python
i0 = raw.rfind("CHAPTER I. I GO TO STYLES")	#return 位置数int
print raw[i0:i0+10]
i1 = i1+6 # this is really the index we want
print raw[i1:i1-7:-1]	#倒着来
```

### 

## Paramiko

```python
import paramiko
host='192.168.2.10'
port=22
name='gpu'
passwd='talent2012'
cmd=['/vload/bin/secv_shell','display version']
s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(host,port,username=name,password=passwd)
#stdin,stdout,stderr=s.exec_command('/root/test.sh')
stdin,stdout,stderr=s.exec_command('cd kaldi/egs/aidatatang_asr;python3 run_sh.py testAudio/Database/ResDB3.db test3')
# stdin.write("Gpu001\n")
# # stdin.flush()
out=stdout.readlines()
print(out)
for o in out:
    print(o)
```