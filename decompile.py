import sys
from grammar import grammar


#Recusive decompile

def redecompile(source, grammar, code):
	if grammar.nonTerminatatingSymbols&set(code):
		symbol = filter(lambda x:x in grammar.nonTerminatingSymbols, code)[-1]
		rules = grammar.rules[symbol]
		replacement = rules[source%len(rules)]
		return redecompile(source/len(rules), grammar, code[::-1].replace(symbol,replacement,1)[::-1])
	else:
		return code

def decompile(source, grammar):
	return redecompile(source, grammar, grammar.headSymbol)

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Please provide an input file and number of bits to read."
	else:
		f = open(sys.argv[1])
		source = int("".join(format(ord(x), 'b') for x in f.read())[:int(sys.argv[2])],2)
		print source
