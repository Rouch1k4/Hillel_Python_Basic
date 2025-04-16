def add_one(some_list):
    str_digit = [str(d) for d in some_list]
    result = ''.join(str_digit)
    result = int(result)
    result += 1
    final_list = [int(d) for d in str(result)]
    return final_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

