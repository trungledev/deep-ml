def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	m = len(a)
	n = len(a[0])
	length = len(b)
	if n != length:
		return -1
	result = [sum(x * y for x, y in zip(row, b)) for row in a]
			
	return  result