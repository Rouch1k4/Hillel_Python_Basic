
def common_elements():
	multiple_3 = {x for x in range(100) if x % 3 == 0}
	multiple_5 = {x for x in range(100) if x % 5 == 0}

	common = multiple_3 & multiple_5

	return common

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
