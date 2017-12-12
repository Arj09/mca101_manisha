def evilNumber(num):
	count = 0
	binnum  = bin(num)
	length = len(binnum)

	for i in range(2,length):
		if binnum[i] == '1':
			count += 1

	if count % 2 == 0:
		return True
	else:
		return False
