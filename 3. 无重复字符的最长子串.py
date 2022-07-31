s = "abcabcbb"
if s:
  num_list = []
  for i in range(len(s)-1):
    num = 1
    num_list.append(num)
    for j in range(i+1, len(s)):
      if s[j] in s[i:j]:
        break
      else:
        num = num + 1
        num_list.append(num)
        continue
  if num_list:
    print(max(num_list))