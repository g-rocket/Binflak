import sys

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Please provide an input file and number of bits to read."
	else:
		f = open(sys.argv[1])
		source = int("".join(format(ord(x), 'b') for x in f.read())[:int(sys.argv[2])],2)
		print source
		
