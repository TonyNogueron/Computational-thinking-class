def sum(l1, l2, target):
  diff = target
  diff2 = target
  answer1 = []
  answer2 = []

  for i in l1:
    for j in l2:
      if i + j == target:
        return (i , j)
      elif i + j < target:
        if (target - (i+j)) < diff:
          diff = target - (i+j)
          answer1 = [i, j]
      elif i + j > target:
        if ((i+j) - target) < diff2:
          diff2 = (i + j) - target
          answer2 = [i,j]
  if diff == diff2:
    return (answer1[0], answer1[1]), (answer2[0], answer2[1])
  elif diff < diff2:
    return (answer1[0], answer1[1])
  else:
    return (answer2[0], answer2[1])

l1 = [-1, 3, 8, 2, 9, 5]
l2 =[4, 1, 2, 10, 5, 20]

target = 24

print(sum(l1,l2,target))