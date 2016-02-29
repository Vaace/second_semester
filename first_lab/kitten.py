import sys
import os


temp = 0
for arg in sys.argv:
	temp += 1
	if os.path.exists:
		if (os.path.isfile) and (temp > 1):
			input = open(arg, 'r')
			filey = input.readlines()
			for i in filey:
				print(i)
			input.close()	
