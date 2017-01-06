from ebin import expandEBin

closeMap = {
	"(" : ")",
	"[" : "]",
	"{" : "}",
	"<" : ">",
}

charMap = {
	1 : "(",
	2 : "[",
	3 : "{",
	4 : "<",
}

def decompileEBin(binSource, debug = False):
	brainSource = ""
	openParenStack = []
	while (binSource > 0) or (len(openParenStack) > 0):
		binChar = binSource % 5
		binSource //= 5
		
		if debug: print(binChar)
		
		if (binChar == 0) and (len(openParenStack) > 0):
			# closing enclosing glyph
			brainSource += closeMap[openParenStack.pop()]
		else:
			brainSource += charMap[binChar]
			openParenStack.append(charMap[binChar])
	return brainSource

def decompile(binSource, debug = False):
	return decompileEBin(expandEBin(binSource), debug)

if __name__ == "__main__":
	pass
