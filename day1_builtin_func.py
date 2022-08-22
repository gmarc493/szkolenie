# coding: utf-8
world = 'World'
world
print(f'Hello {world}!')
import script
script
script.world
world.upper()
script.upper()
script.upper
# immutable: str, int, float, (numerical), tuple, frozenset, bool, None
x = 12
x += 30
x
# x = x + 30
world
hellp = 'Hello'
hello = 'Hello'
hello2 = hello
hello2 is hello
hello += ' World!'
hello
hello2 is hello
hello
hello2
t = (1, 2)
t += (3, 4)
t
hello2 is hellp
x = 12
y = 10 + 2
x is y
x = 30000
y = 10000 + 20000
x is y
type(x) is int
x is None
x is not None
x is True
2 in t
'll' in hello
'oo' in hello
'e' in hello
import foo
import sys
sys.path
import foo
foo.x
foo.y
foo
None
type(None)
x = None
x is None
x == None
hello
'Hello World!' == hello
'Hello World!' is hello
True
False
type(True)
x is Trie
x is True
x == True
x
x = 12
x is True
x == True
x
x = 1
x is True
x == True
x == True
0 == False
1 == False
1 == True
10 + True
issubclass(bool, int)
bool(123)
bool(-23)
bool(0)
bool(0.0)
bool('foo')
bool('False')
bool('')
bool([1])
bool([False])
bool([])
bool({})
bool(None)
foo
import foo
import foo
import foo
import script
sys
sys.path
sys.path.insert(0, '/home/jlg/src/tools/)
sys.path.insert(0, '/home/jlg/src/tools/')
sys
sys.path
sys.path.pop(0)
sys.path
import sys
l1 = [1, 2, 3]
l1 = [1, 2.1, 'foo']
l2 = l1
l2 is l1
l2 == l1
l1.append('bar')
l1
l2
l2.pop()
l2
l1
l1
lcopy = l1.copy()
lcopy
l1
lcopy == l1
lcopy is l1
lcopy.pop()
lcopy
l1
lcopy = list(l1)
l1
l1[0]
l1[1]
l1[2]
l1[0:2]
l1[0:]
l1[:]
import copy
copy.copy(l1)
embeded = ['inside', 42]
l1 = [1, 2.1, 'foo', embeded]
l1
embeded.append(None)
embeded
l1
lcopy = list(l1)
lcopy
lcopy.append(True)
lcopy
l1
embeded.pop()
embeded
l1
lcopy
import copy
copy.deepcopy
ldeep = copy.deepcopy(l1)
ldeep
embeded.pop()
embeded
l1
ldeep
t = (1, 2)
t += (3, 4)
l = [1, 2]
l += [3, 4]
l
ll = l
ll
l
l += [5, 6]
ll
l
keep_running = True
def loop_me(run):
    for x in range(10):
        if not run:
            break
        print(x)
        
    
loop_me(keep_running)
import threading
#on fucntion call loop_me(keep_running) -> run = keep_running
keep_running = False
keep_running = [True]
def loop_me(run):
    for x in range(10):
        if not run[0]:
            break
        print(x)
        
keep_running[0] = False
keep_running = [False]  # this wouldn't change the state in loop_me
def loop_me():
    for x in range(10):
        if not keep_running:
            break
        print(x)
        
# list, set, dict, class
# mustable: list, set, dict, class
# mutable: list, set, dict, class
True or False
True and False
True and not_existent_name
True or no_existent_name
True and not_existent_name
False and not_existent_name
1 or 0
bool(1)
'str' or []
[] and no_such
2 and 'marcin'
2 and ''
0 and 'marcin'
bool(0 and 'marcin')
bool(2 and 'marcin')
if 2 and 'marcin':
    print('all are true')
    
if 0 and 'marcin':
    print('not all are true')
    
True or False and True
True or False and False
True or (False and False)
(True or False) and False
0 and 1 or 'marcin'
(0 and 1) or 'marcin'
0 and 1
1 or 'marcin
1 or 'marcin
1 or 'marcin'
0 or 'marcin'
# int val = cond ? trueval : falseval
val = 'true val' if x == 12 else 'falseval'
val
x
x = 12
val = 'true val' if x == 12 else 'falseval'
vale
val
default = None
val = default or ['my default value']
vale
val
default = 'user value'
val = default or ['my default value']
val
default = ''
val = default or ['my default value']
val
user_data = input('What is your name? ')
user_data
user_data = input('What is your name? ')
user_data
name = user_data or 'Stranger'
print(f'Hello {name}!')
user_data = input('What is your name? ')
print(f'Hello {name}!')
name = user_data or 'Stranger'
print(f'Hello {name}!')
names = ['Bob', 'Dan', 'Carol', 'alice', 'erin']
name
for name in names:
    print(name)
    
for name in names:
    print(name.title())
    
for i in range(7):
    print(i)
    
# for i = 0; i < N; i++ 
for i in range(len(names)):
    print(i, names[i])
    
for pair in enumerate(names):
    print(pair[0], pair[1])
    
for i, name in enumerate(names):
    print(i, name)
    
list(range(6))
list(range(3, 6))
list(range(3, 8, 2))
from calendar import month_name
get_ipython().run_line_magic('pinfo', 'month_name')
month_name
month_name(0)
month_name(1)
month_name
month_name[0]
month_name[1]
list(month_name)
MONTHS = list(month_name)
MONTHS.pop(0)
MONTS
MONTHS
for i, name in enumerate(MONTHS):
    print(i, name)
    
for i, name in enumerate(MONTHS, start=1):
    print(i, name)
    
for i, name in enumerate(MONTHS, start=-1500):
    print(i, name)
    
names
roles = ['ceo', 'cfo', 'cto', 'swe', 'sre', 'qa]
roles = ['ceo', 'cfo', 'cto', 'swe', 'sre', 'qa']
names
roles
zip(names, roles)
list(zip(names, roles))
for name, role in zip(names, roles):
    print(f'{name} is our {role}')
    
for name, role in zip(names, roles):
    print(f'{name.capitalize()} is our {role.upper()}')
    
for i, name in zip(range(1, 1000000000000000000000000),  MONTHS):
    print(i, name)
    
import itertool
import itertools
itertools.count
get_ipython().run_line_magic('pinfo', 'itertools.count')
help(itertools.count)
get_ipython().run_line_magic('pinfo', 'itertools.count')
get_ipython().run_line_magic('pinfo', 'itertools.count')
for i, name in zip(itertools.count(start=1),  MONTHS):
    print(i, name)
    
zip(itertools.count(start=1), itertools.count(start=1))
i = 0
for _ in itertools.count(start=1):
    i += 1
    if i > 10000000:
        break
        
i
for i, name, role in zip(itertools.count(), names, roles):
    print(f'{i} -> {name.capitalize()} is our {role.upper()}')
    
len(name)
name
name[0]
name[1]
names
len(names)
names[0]
names = ('Bob', 'Dan', 'Carol', 'alice', 'erin')
len(names)
names[2]
for name, role in zip(names, roles):
    print(f'{name.capitalize()} is our {role.upper()}')
    
s = 'abcdef'
len(s)
s[1]
for ch in s:
    print(ch)
    
names
list(names)
list(s)
s
tuple(s)
name
names
names = list(names)
names
names.sort()
names
'Bob' < 'Carol'
l = [1, 32, 11.2, 44]
l.sort()
l
1 < 11.2
l = [1, 32, 11.2, 44, '']
l.sort()
44 < ''
'' < 44
[0, True, False, 1]
l = [0, True, False, 1]
l.sort()
l
l.sort(reverse=True)
("")
l
names = ('Bob', 'Dan', 'Carol', 'alice', 'erin')
names.sort()
sorted(names)
names
sorted(;)
sorted(;)
sorted(l)
sorted(l, reverse=True)
sorted(names, reverse=True)
sorted_names = sorted(names)
l = [1, -3, 43, 3, 17]
sorted(l)
l = [1, -3, 43, 3, -17]
sorted(l)
abs(12)
abs(-12)
sorted(l, key=abs)
def mod3(x):
    return x % 3
    
sorted(l, key=mod3)
(1, 'foo') < (2, 'bar')
(3, 'foo') < (2, 'bar')
(2, 'foo') < (2, 'bar')
(2, 'foo') < (2, 'gar')
names
sorted(names)
#sorted(names, key=to_lower)
def to_lower(x):
    return x.lower()
    
sorted(names, key=to_lower)
sorted(l, key=lambda x: x % 3)
sorted(names, key=lambda x: x.lower())
'alice'.lower()
'Bob'.lower()
'Carol'.lower()
MODULATOR = 3
sorted(l, key=lambda x: x % MODULATOR)
cached_func = lambda x: x % MODULATOR
cached_func
MODULATOR = 4
MODULATOR = 2
sorted(l, key=cached_func)
lambda: None
(lambda: None)()
(lambda x: 1/x)(2)
(lambda x, y: x / y)(2, 1)
(lambda x, y: x / y)(1, 2)
(lambda *args: sum(args))(1, 2, 4,2 ,2,3,2,432,4,45,43)
sorted(l, key=lambda: None)
sorted(l, key=lambda x, y: None)
l
map(abs, l)
list(map(abs, l))
l
list(map(lambda x: x % 3, l))
list(map(lambda x: x % 2, l))
list(map(lambda x: x.lower(), names))
abs
def to_lower(x):
    return x.lower()
    
to_lower
to_lower('Foo')
to_lower
func = to_lower
func
func()
func('Bar')
type(to_lower)
type(to_lower) is function
import inspect
inspect.isfuction(to_lower)
inspect.is_fuction(to_lower)
inspect.isfunction(to_lower)
from typing import Callable
isinstance(to_lower, Callable)
list(map(lambda x: x.lower(), names))
result = []
result = []
for item in names:
    mapped = item.lower()
    result.append(mapped)
    
result
[x.lower() for x in names]
[x % 3 for x in l]
[abs(x) for x in l]
map(abs, l)
list(map(abs, l))
{abs(x) for x in l}
tuple(abs(x) for x in l)
(abs(x) for x in l)
g =(abs(x) for x in l)
g = (abs(x) for x in l)
g
for item in g:
    print(item)
    
g = (abs(x) for x in l)
list(g)
g = (abs(x) for x in l)
tuple(g)
g = (abs(x) for x in l)
g
list(g)
list(g)
[abs(x) for x in l]
l
[(abs(x), x) for x in l]
sorted([(abs(x), x) for x in l])
sorted((abs(x), x) for x in l)
tmp = sorted((abs(x), x) for x in l)
tmp
for pair in tmp:
    pair[1]
    
for pair in tmp:
    print(pair[1])
    
for abs_, orig in tmp:
    print(orig)
    
abs
abs_
orig
def print(text):
    print(f'<p>{text}</p>')
    
print('Python')
del print
print('Python')
del print
print('Python')
print
get_ipython().run_line_magic('pinfo', 'print')
def print_(text):
    print(f'<p>{text}</p>')
    
print_('Python')
def print_html(text):
    print(f'<p>{text}</p>')
    
tmp
sorted((abs(x), x) for x in l)
for abs_, orig in tmp:
    print(orig)
    
for _, orig in tmp:
    print(orig)
    
_
result = []
for _, orig in tmp:
    result.append(orig)
    
result
l
[orig for _, orig in tmp]
[orig for _, orig in sorted((abs(x), x) for x in l)]
sorted(l, key=abs)
l
l = [1, 3, 43, -3, -17]
[orig for _, orig in sorted((abs(x), x) for x in l)]
sorted(l, key=abs)
k = [1, -1.2, '432', 0]
sorted(k)
sorted(k, key=float)
k = [1, -1.2, '432', 0, 'foo']
sorted(k, key=float)
[(abs(x), x) for x in l]
{abs(x): x for x in l}
{x: abs(x) for x in l}
dict((abs(x), x) for x in l)
text = 'FooBarBaz'
[ch for ch in text]
list(text)
[ch + 'eey' for ch in text]
[ch + 'arrr' for ch in text]
[ch for ch in text]
[ch for ch in text if ch.islower()]
[ch for ch in text if ch.isupper()]
l
[x for x in l if l % 2 == 9]
[x for x in l if l % 2 == 0]
[x for x in l if x % 2 == 0]
l
[x for x in l if x % 2 == 1]
[x for x in l if x % 3 == 0]
[ch for ch in text if ch.isupper()]
[ch + 'arrr' for ch in text if ch.isupper()]
result = []
for ch in text:
    if ch.isupper():
        result.append(ch + 'arrr')
        
result
for ch in 'abc':
    for x in range(3):
        print(ch, x)
        
result = []
for ch in 'abc':
    for x in range(3):
        result.append(f'{ch}{x}')
        
result
[f'{ch}{x}' for ch in 'abc' for x in range(3)]
[f'{ch}{x}' for ch in 'abc' for x in range(3) if x % 2 == 0 and ch > 'a']
result = []
for ch in 'abc':
    for x in range(3):
        #if 
        result.append(f'{ch}{x}')
        
[f'{ch}{x}'
 for ch in 'abc'
 for x in range(3)
 if x % 2 == 0 and ch > 'a']
[f'{ch}{x}'
 for ch in 'abc'
     for x in range(3)
         if x % 2 == 0 and ch > 'a']
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix
[x**2 for row in matrix for x in row]
result = []
for row in matrix':
    for x in row:
        result.append(x**2)
result = []
for row in matrix:
    for x in row:
        result.append(x**2)
        
[x**2 for row in matrix for x in row]
result
result = []
for row in matrix:
    new_row = []
    for x in row:
        new_row.append(x**2)
    result.append(new_row)
    
result
result = []
for row in matrix:
    new_row = [x**2 for x in row]
    result.append(new_row)
    
result
result = []
for row in matrix:
    result.append([x**2 for x in row])
    
result
[[x**2 for x in row] for row in matrix]
for i in range(10):
    pass
    
i
j
[j for j in range(10)]
j
[[x**2 for x in row if x % 2 == 0] for row in matrix]
[[x**2 for x in row if x % 2 == 0] for row in matrix if sum(row) < 10]
[[x**2 for x in row if x % 2 == 0] for row in matrix if sum(row) < 20]
[[x**2 for x in row] for row in matrix if sum(row) < 20 and x % 2 == 0]
x
del x
[[x**2 for x in row] for row in matrix if sum(row) < 20 and x % 2 == 0]
# unpacking
a = 1
b = 2
tmp = a
a = b
b = tmp
a
b
a, b = b, a
a
b
b, a
(b, a)
b, a
t = b, a
t
a, b = t
a
b
a, b = 5, 6
a
b
a, b = [5, 6]
a, b = (5, 6)
a, b = t
l
a, b, c, d, e = l
a
e
a, b, c, d = l
a, b, c, d, e, f = l
for i, name in enumerate(MONTHS, start=1):
    print(i, name)
    
    
    
for pair in enumerate(MONTHS, start=1):
    i, name = pair
    print(i, name)
    
a, b, c, d = [1, 2, 3, 4]
d
a
a, b, c, d = l
a, b, c, *d = [1, 2, 3, 4, 5, 6]
a
b
c
d
a, b, c, *d = [1, 2, 3, 4]
d
a, b, c, *d = [1, 2, 3]
d
a, b, c, *d = [1, 2]
a, b, *c, d = [1, 2, 3, 4, 5, 6]
c
d
a, *b, c, d = [1, 2, 3, 4, 5, 6]
b
c
*a, b, c, d = [1, 2, 3, 4, 5, 6]
a
a, *b, c, d = [1, 2, 3]
b
c
d
passwd = 'mark:x:1001:1001:fullname:home:shell'
passwd.split(':')
row = passwd.split(':')
user, _, uid, gid, _, home, _ = passwd.split(':')
user, _, uid, gid, _, _,  _ = passwd.split(':')
user, _, uid, gid, *_ = passwd.split(':')
_
a, b = [1, (2, 3)]
a
b
a, (b, c) = [1, (2, 3)]
a
b
c
{'foo': 'bar', 'baz': 'cux')
{'foo': 'bar', 'baz': 'cux'}
dict = {'foo': 'bar', 'baz': 'cux'}
del dict
d = {'foo': 'bar', 'baz': 'cux'}
for key in d:
    print(key)
    
for key in d.keys():
    print(key)
    
for x in d.values():
    print(x)
    
for x in d.items():
    print(x)
    
for k, v in d.items():
    print(k, v)
    
for i, item in enumerate(d.items()):
    print(i, item)
    
for i, (k, v) in enumerate(d.items()):
    print(i, k, v)
    
for i, k, v in enumerate(d.items()):
    print(i, k, v)
    
for i, (k, v) in enumerate(d.items()):
    print(i, k, v)
    
matrix
for a, b, c in matrix:
    print(a, b, c)
    
data = [[(1, 2), 'label1'], [(4, 5), 'label2'], [(7, 8), 'label3']]
len(data)
for (a, b), label in data:
    print(a+b, label)
    
for features, label in data:
    print(sum(features), label)
    
data = [[1, 2, 'label1'], [4, 5, 'label2'], [7, 8, 'label3']]
for a, b, label in data:
    print(a+b, label)
    
for *features, label in data:
    print(features, label)
    
for *features, label in data:
    print(sum(features), label)
    
for *features, label in data:
    print(max(features), label)
    
for *features, label in data:
    print(min(features), max(features), sum(features) / len(features), label)
    
import math
import itertools
math.mean
import statistics
get_ipython().run_line_magic('pinfo', 'statistics.mean')
for *features, label in data:
    print(min(features), max(features), statistics.mean(features), label)
    
data = [[1, 2, 1, 1, 1 'label1'], [4, 32, 5, 'label2'], [7, 8, 3, 4, 5, 'label3']]
data = [[1, 2, 1, 1, 1, 'label1'], [4, 32, 5, 'label2'], [7, 8, 3, 4, 5, 'label3']]
for *features, label in data:
    print(min(features), max(features), statistics.mean(features), label)
    
def echo(a, b):
    print(a, b)
    
echo
echo()
a, b = 1, 2
echo(1, 2)
echo(1,)
echo(1, 2, 3)
def echo(a, b):
    print(a, b)
    return
    
retval = echo(1, 2)
retval is None
print(retval)
None
l.sort(reverse=True)
print('foo')
retval = print('foo')
print(retval)
def echo(a, b):
    return
    print(a, b)
    return
    
echo(1, 2)
def echo(a, b):
    if a > 10:
        return
    print(a, b)
    
def echo(a, b):
    if a > 10:
        return
    print(a, b)
    
echo(1, 2)
echo(11, 2)
def echo(a, b):
    if a > 10:
        a = 10
    print(a, b)
    
echo(7, 2)
echo(17, 2)
def max_(a, b):
    if a > bL
def max_(a, b):
    if a > b:
        return a
    return b
    
max_(4, 3)
max_(4, 13)
bigger = max_(4, 13)
bigger
def pair():
    return 1, 2
    
pair()
a, b = pair()
a
b
max_(4, 13)
max_(a=4, b=13)
max_(b=13, a=4)
def max_(a, b):
    if a > b:
        return a, 'a'
    return b, 'b'
    
max_(4, 13)
max_(a=4, b=13)
max_(b=13, a=4)
max_(4, b=13)
max_(4, a=13)
a, b, *c = [1, 2, 3, 4]
a
v
a
b
c
def echo(a, b, *c):
    print(a, b, c)
    
echo(1, 2, 3, 4)
echo(1, 2)
echo(1, 2, 2)
echo(1, 2, 3, 2, 2, 2, 2)
def echo(*args):
    print(args)
    
echo(1, 2, 3, 2, 2, 2, 2)
echo(a=1)
echo(**kwargs)
def echo(**kwargs):
    print(kwargs)
    
    
echo(1, 2, 3)
echo(a=1, b=2, c=3)
def echo(*args, **kwargs):
    print(args, kwargs)
    
echo(4, 5, 6, a=1, b=2, c=3)
get_ipython().run_line_magic('pinfo', 'sorted')
sorted(k, key=float)
sorted(l, key=abs)
sorted(l, abs)
sorted(l, key=abs)
def only_kw(*, b, c):
    echo(b, c)
    
only_kw(1, 2)
only_kw(b=1, c=2)
def only_kw(*, b, c):
    print(b, c)
    
def default(b=None, c=None):
    print(b, c)
    
default()
default(1)
default(1, 2)
default(b=3)
default(c=3)
def default(*, b=None, c=None):
    print(b, c)
    
default()
default(1)
default(1, 2)
def default(pos1, pos2, *, b=None, c=None):
    print(pos1, pos2, b, c)
    
default(1, 2)
default(1, 2, b=12)
default(1, 2, 12)
default(1, 2)
default(pos1=1, pos2=2)
def default(pos1, pos2, /, mix, *, b=None, c=None):
    print(pos1, pos2, mix, b, c)
    
default(pos1=1, pos2=2)
default(pos1=1, pos2=2, mix=3)
default(1, 2, mix=3)
default(1, 2, 3)
def default(pos1, pos2, /, mix=None, *, b=None, c=None):
    print(pos1, pos2, mix, b, c)
    
def default(pos1, pos2=None, /, mix=None, *, b=None, c=None):
    print(pos1, pos2, mix, b, c)
    
default(1)
default(1, 2)
default(1, 2, 3)
default(1, 2, mix=3)
