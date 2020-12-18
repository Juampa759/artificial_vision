aux = []

numbers = [5,3,8,10,20,2,4,1]

def reverse_numbers():
	last_pos = len(numbers)-1

	while last_pos >=0:
		aux.append(numbers[last_pos])
		last_pos -=1

	return aux

#print(numbers)
res = reverse_numbers()
print(res)