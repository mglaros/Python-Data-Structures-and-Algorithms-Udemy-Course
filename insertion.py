def insertion_sort(nums):
	for i in range(len(nums)):
		j = i 

		while j>0 and nums[j-1] > nums[j]:
			swap(nums, j-1, j)
			j = j - 1

	return nums 


def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp 


if __name__ == "__main__":
	a = [-1,-3,-2,0]
	print(insertion_sort(a))