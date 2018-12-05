from random import randint
import array as arr
a = arr.array('i',[1,2,3])

a[0]=randint(0,9) #change
a[1]=randint(0,9)
a[2]=randint(0,9)
print(a)
a.append(4) 
print(a)
a.extend([5,6,7])
print(a)

print(a[0])
print(a[1])
print(a[-1])
