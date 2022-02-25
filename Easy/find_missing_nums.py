nums = [0,1,2,4,5] 
def missing_num(nums):
	num = 0
	for i in range(len(nums)):
		if num not in nums:
			return num
		else:
			num = num +1

print(missing_num(nums))