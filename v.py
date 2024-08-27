def b(a):
  u_count=0
  l_count=0
  for i in a:
    if i.isupper():
      u_count +=1
    elif i.islower():
      l_count +=1
  print('No. of Upper case characters:' + str(u_count))
  print('No. of lower case characters:' + str(l_count))
a='The quick Brow Fox'
b(a)