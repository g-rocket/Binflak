import math

def eBinIsValid(binSource):
	nestingLevel = 0
	while binSource > 0:
		binChar = binSource % 5
		binSource //= 5
		if binChar > 0:
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

def numValidLT(source, debug=False):
	sourceL = []
	while source > 0:
		sourceL.append(source % 5)
		source //= 5
	data = [1]
	numValidSequences = 0
	currentDepth = 0
	totalDepth = sum((1 if thisChar > 0 else -1) for thisChar in sourceL)
	currentLength = 0
	shorterSeqs = 0
	if debug:
		print(str(sourceL) + ": " + str(currentDepth))
	for thisChar in sourceL:
		data2 = [4**((currentLength+1)//2 + i) * x for i,x in enumerate(data)]
		shorterSeqs += data2[-1]
		if debug:
			print("%d: %s -> %s" % (currentLength, data, data2))
		
		for ltChar in range(thisChar):
			if ltChar == 0 and currentLength == len(sourceL) - 1:
				if debug:
					print("adding %d (final 0)" % shorterSeqs)
				numValidSequences += shorterSeqs
			else:
				newDepth = currentDepth + (1 if ltChar > 0 else -1)
				if debug:
					print("%s -> %s (%d -> %d, %d)" % (thisChar, ltChar, currentDepth, newDepth, (totalDepth + newDepth)))
				if newDepth >= 0:
					if debug:
						print("adding %s" % data2[min(0, -(totalDepth + newDepth)//2):])
					numValidSequences += sum(data2[min(0, -(totalDepth + newDepth)//2):])
		#if debug:
		#	print("adding " + str(thisChar) + " * " + str([
		#		4**((currentLength+1)//2 + i)*x 
		#		for i,x in enumerate(data)]) +
		#		" starting at " + str(currentDepth//2))
		#numValidSequences += thisChar*sum(
		#	4**((currentLength+1)//2 + i)*x 
		#	for i,x in enumerate(data))
		
		currentDepth += (1 if thisChar > 0 else -1)
		currentLength += 1
		
		lastRow = data
		offset = -1 if (currentLength % 2 == 0) else 1
		data = [getOrZero(lastRow, i) + getOrZero(lastRow, i + offset)
			for i in range(currentLength//2 + 1)]
	return numValidSequences

def getOrZero(list, index):
	return list[index] if 0 <= index < len(list) else 0
