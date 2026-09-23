def NDW(list1,dep = 0):
	if type(list1) == int:
		return (list1 * dep)
	sum = 0
	for v in list1:
		sum += NDW(v,dep + 1)
	return (sum)
