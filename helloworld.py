import sys

n = 0
i = 0
for arg in sys.argv:
	i += 1
	if (len(arg) % 3 == 0) and (i != 1):	
		n +=1
print(n)
