def merge(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	left = []
	right = []
	for i in range(1, n1):
		left[i] = A[p + i - 1]
	for j in range(1, n2):
		right[j] = A[q + j]
	i = 1
	j = 1
	for k in range(p, r): 
		if left[i] <= right[j]:
			A[k] = left[i]
			i += 1
		else:
			A[k] = right[j]
			j += 1

def merge_sort(A, p, r):
	if p < r:
		q = (p + r)/2
		merge_sort(A, p, q)
		merge_sort(A, q + 1, r)
		merge(A, p, q, r)
	return A

A = [3,2,45,5,9,0]
A = merge_sort(A, 0, len(A)-1)
print(A)

