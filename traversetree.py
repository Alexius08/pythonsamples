inputarr=[1,[2,3],[[4],5]]
newarr=[]
level=[inputarr]
while (level!=[]):
  if(isinstance(level[len(level)-1],list)):
    if(len(level[len(level)-1])>0):
      level.append(level[len(level)-1].pop(0))
    else:
      level.pop()
  else:
    newarr.append(level.pop())
  print("Sorted")
  print(newarr)
  print("Unsorted")
  print(level)