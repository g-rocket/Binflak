class grammar(object):
	def __init__(self,text):
		self.rules = dict(map(lambda x: (x.split("->")[0].strip(),x.split("->")[1].strip().split("|")),text.strip().split("\n")))
		self.nonTerminatingSymbols = self.rules.keys()
	def size(self,nts):
		return len(self.rules[nts])

if __name__ == "__main__":
	grammar('''
S -> ()|[]|<>|{}|(S)|<Z>|[S]|{S}|()S|[]S|<>S|{}S|(S)S|<Z>S|[S]S|{S}S
Z -> <>|{}|(S)|{Z}|<>Z|{}Z|(S)Z|{Z}Z
''')
