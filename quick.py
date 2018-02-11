def quick_sort(nums, low, high):
	if low >= high:
		return

	pivot = partition(nums, low, high)
	quick_sort(nums, low, pivot-1)
	quick_sort(nums, pivot+1,high)


def partition(nums, low, high):
	pivotIndex = (low + high)//2
	swap(nums,pivotIndex, high)
	i = low

	for j in range(low,high):
		if nums[j] <= nums[high]:
			swap(nums, i, j)
			i = i + 1 

	swap(nums, i, high)
	return i 



def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp 


if __name__ == "__main__":
	a = [5,3,2,7,8,3,4,6]

	quick_sort(a, 0, len(a) - 1)

	print a 