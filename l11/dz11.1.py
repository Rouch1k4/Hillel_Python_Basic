def prime_generator(end):
    for number in range(2, end + 1):
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            yield number

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
