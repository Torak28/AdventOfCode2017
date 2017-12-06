def divideF(x, tab):
	ret = []
	print(x, tab)
	while sum(ret) != x:
		print(ret)
		ret.append(x // (len(tab) - 1))
		if x % (len(tab)-1) == 1 and sum(ret) == (x - 1):
			ret.append(1)
	return ret

divideF(13, [13, 6, 2, 13, 8, 2, 8, 1, 13, 5, 8, 11, 8, 5, 6, 9])