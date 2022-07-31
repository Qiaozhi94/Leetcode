a = '2'
print(a)   # '2'
print(type(a))   # <class 'str'>
b = int(a)
print(b)   # 2
print(type(b))   # <class 'int'>
c = str(b)
print(c)   # '2'
print(type(c))   # <class 'str'>
# --------------------------------
d = [1,2]
e = tuple(d)
print(e)   # (1, 2)
print(type(e))   # <class 'tuple'>
f = list(e)
print(f)   # [1, 2]
print(type(f))   # <class 'list'>


g = [-1,-3,-4,-3,2,-9,-8]
h = []
for i in range(len(g)):
        h.append(abs(g[i]))

h.sort()
print(h)