numbers = input().split(' ')
nums = [int(num) for num in numbers]


dict = {}

for i in range(len(nums)):
    if (nums[i] in dict):
        dict[nums[i]] += 1
    else:
        dict[nums[i]] = 1

print(max(dict, key=dict.get))