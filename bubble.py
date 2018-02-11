def bubble_sort(nums):
	for i in range(len(nums) - 1):
		for j in range(len(nums) - 1 - i):
			if nums[j] > nums[j+1]:
				swap(nums, j, j+1)

	return nums 


def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp


if __name__ == "__main__":
	a = [1,5,3,2,4,8,7]
	print(bubble_sort(a))

