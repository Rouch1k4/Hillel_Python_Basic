import string

alphabet = input("Type your diapason e.x a-T / Z-s : ")
start,end = alphabet.split('-')
start = string.ascii_letters.index(start)
end = string.ascii_letters.index(end)
result = string.ascii_letters[start:end + 1]
print (result)
