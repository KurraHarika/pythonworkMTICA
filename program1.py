Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello'"world"'today'
'helloworldtoday'
a="hello""world"'python'
a
'helloworldpython'
type(a)
<class 'str'>
a="hello","world","python"
a
('hello', 'world', 'python')
typr(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    typr(a)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(a)
<class 'tuple'>
a=23,7.9,'python',5+8j,'c'
a
(23, 7.9, 'python', (5+8j), 'c')
a=(5)
b=(5.8)
c=('hello')
type(a)
<class 'int'>
a=(%)
SyntaxError: invalid syntax
a=(5,)
type(a)
<class 'tuple'>
type(5.8)
<class 'float'>
type(c)
<class 'str'>
type(b)
<class 'float'>
type(lst1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    type(lst1)
NameError: name 'lst1' is not defined
lst1=list()
type(lst1)
<class 'list'>
lst1.append(10)
las1
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    las1
NameError: name 'las1' is not defined
lst1
[10]
las1.append(15)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    las1.append(15)
NameError: name 'las1' is not defined
lst1.append(15)
lst1.append(10)
lst1
[10, 15, 10]
lst1.append('python')
lst1
[10, 15, 10, 'python']
lst1.clear()
lst1
[]
lst1=[10,15,10,'python']
lst1.count(10)
2
lst1.count(15)
1
lst1.count('python')
1
lst1.count('Pyhon')
0
lst1.count(25)
0
len(lst1)
4
