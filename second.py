#nutakoe
import argparse
import sys
parser = argparse.ArgumentParser (
	description = 'calculator'
)
parser.add_argument(
	'values',
	metavar='VALUES',
	type = float,
	nargs=2,
	help='input data'
)
parser.add_argument(
	'-a',
	'--action',
	metavar = 'ACTION',
	type = str,
	action = 'store',
	help = 'arithmetic action'
)	
parser.add_argument(
	'-v',
	'--verbose',
	action = 'store_true',
	help = 'show the expression'
)

args = parser.parse_args()
#if not args.action:
#	print( file=sys.stderr )
#	sys.exit(-1)

x = args.values[0]
y = args.values[1]

if not args.verbose:
	if args.action == '+':
		print(x + y)
	elif args.action == '-':
		print(x - y)
	elif args.action == '*':
		print(x*y)
	elif args.action == '/':
		print(x/y)			
else:
	if args.action == '+':
		print(str(x)+args.action+str(y)+'='+str(x + y))
	elif args.action == '-':
		print(str(x)+args.action+str(y)+'='+str(x - y))
	elif args.action == '*':
		print(str(x)+args.action+str(y)+'='+str(x * y))
	elif args.action == '/':
		print(str(x)+args.action+str(y)+'='+str(x / y))
