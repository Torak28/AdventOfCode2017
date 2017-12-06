def divideF(x, tab):
	ret = []
	while sum(ret) != x:
		if x // (len(tab) - 1) != 0:
			ret.append(x // (len(tab) - 1))
			if x % (len(tab) - 1) == 1 and sum(ret) == (x - 1):
				ret.append(1)
		else:
			ret.append(1)
	return ret

def distribute(tab, x, i):
	it = i + 1 
	while len(x) != 0:
		if it == len(tab):
			it = 0
		tab[it] = tab[it] + x.pop(0)
		it = it + 1
	return tab

inp = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"

tab = [int(_) for _ in inp.split("\t")]

states = []
step = 0

i = 0
while True:
	states.append(tab[:])
	maxB = max(tab)
	i_maxB = tab.index(maxB)
	x = divideF(maxB, tab)
	tab[i_maxB] = 0
	tab = distribute(tab, x, i_maxB)
	step = step + 1
	if tab in states:
		print("Part I: %s\nPart II: %s" % (step, (len(states) - states.index(tab))))
		break