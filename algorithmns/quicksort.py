def quicksort(arr):
	if len(arr) < 2:
		return arr

	pivot = arr[0]
	
	less = [arr[i] for i in range(len(arr)) if arr[i] < pivot]

	greater = [arr[i] for i in range(len(arr)) if arr[i] > pivot]

	return quicksort(less) + [pivot] + quicksort(greater)

arr = [10, 3, 5, 12, 9, 34, 23]
print(quicksort(arr))
