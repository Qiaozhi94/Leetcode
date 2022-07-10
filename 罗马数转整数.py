from calendar import c
from numpy import append


dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = "LVIII"
a = list(s)
n = len(a)
c = []

for i in range(n):
  b = dict[a[i]]

  c.append(b)
print(c)