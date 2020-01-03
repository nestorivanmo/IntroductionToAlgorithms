A = [5, 2, 4, 6, 1, 3]

def insertion_sort(A, increasing):
	if increasing:
		x = range(1, len(A))
	else:
		x = range(len(A) - 2, -1, -1)
	for j in x:
		key = A[j]
		i = (j - 1) if increasing else (j + 1)
		if increasing:
			while i >= 0 and A[i] > key:
				A[i+1] = A[i]
				i -= 1
			A[i+1] = key
		else:
			while i <= len(A) - 1 and A[i] > key:
				A[i-1] = A[i]
				i += 1
			A[i-1] = key
	return A

A = insertion_sort(A, increasing=False)
print(A)