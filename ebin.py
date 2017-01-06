def eBinIsValid(binSource):
	nestingLevel = 0
	while binSource > 0:
		binChar = binSource % 5
		binSource //= 5
		if(binChar > 0):
			nestingLevel += 1
		else:
			nestingLevel -= 1
		if nestingLevel < 0:
			return False
	return True

def expandEBin(source):
	i = 0
	while i < source:
		i += 1
		if not eBinIsValid(i):
			source += 1
	return source

def compactEBin(source):
	for i in range(source):
		if not eBinIsValid(i):
			source -= 1
	return source
