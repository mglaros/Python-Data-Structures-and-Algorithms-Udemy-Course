def selection_sort(nums):
	for i in range(len(nums)-1):
		index = i
		for j in range(i+1, len(nums)):
			if nums[j] < nums[index]:
				index = j 

		if index != i:
			swap(nums, i, index)

	return nums 


def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp 


if __name__ == "__main__":
	a = [-1,-3,-2,0]
	print(selection_sort(a))