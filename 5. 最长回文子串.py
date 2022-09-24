
s = "safsfdgdfhsdgrh"
#s = "s"
str = s[0]

if len(s) == 1:
  print(s[0])
else:
  for i in range(1, len(s)):
    if s[i-1] == s[i+1]:
      str = s[i-1:i+2]
      j = 2
      while i - j >= 0 and i + j <= len(s):
        if s[i-j] == s[i+j]:
          str = s[i-j:i+j+1]
        else:
          break

print(str)