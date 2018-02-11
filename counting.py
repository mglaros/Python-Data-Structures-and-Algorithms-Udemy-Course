def counting_sort(nums, max, min):
	countArray = (max-min + 1)*[0]

	for i in nums:
		countArray[i-min] = countArray[i-min] + 1


	z = 0

	for i in nums:
		while countArray[i-min] > 0:
			nums[z] = i 
			z = z + 1
			countArray[i-min] = countArray[i-min] - 1 




if __name__ == "__main__":
	a = [5,4,2,6,9,8,20]

	counting_sort(a, 20, 2)

	print a