def sum_re(arr):
	if arr == []:
		return 0

	return arr.pop() + sum_re(arr)

print(sum_re([1, 2, 3, 4]))

def count_items(items):
	if items == []:
		return 0

	items.pop()
	return 1 + count_items(items)

print(count_items([1,2,3,4,5,6,7,8]))

def find_max(nums):
	if len(nums) == 1:
		return nums[0]

	num = nums.pop()
	max = find_max(nums)

	return num if num > max else max

print(find_max([1,20,30,4,5,10]))

def binary_search(nums, target, left, right):
	if left > right:
		return None

	mid = left + (right - left)
	if nums[mid] == target:
		return mid 
	elif nums[mid] > target:
		return binary_search(nums, target, left, mid - 1)
	else:
		return binary_search(nums, target, left + 1, right)

nums = [1, 2, 4, 6, 7, 10, 13, 15, 19]
print(binary_search(nums, 6, 0, len(nums) - 1))
print(binary_search(nums, 20, 0, len(nums) - 1))

