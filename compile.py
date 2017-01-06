import sys
from ebin import compactEBin

charMap = {
	"(" : 1,
	"[" : 2,
	"{" : 3,
	"<" : 4,
	")" : 0,
	"]" : 0,
	"}" : 0,
	">" : 0,
}

def compileEBin(brainSource, debug = False):
	binSource = 0
	multiplier = 1
	for char in brainSource:
		binChar = charMap[char]
		
		if debug: print(binChar)
		
		binSource += binChar * multiplier
		multiplier *= 5
	return binSource

def compile(brainSource, debug = False):
	return compactEBin(compileEBin(brainSource, debug))

if __name__ == "__main__":
	pass
