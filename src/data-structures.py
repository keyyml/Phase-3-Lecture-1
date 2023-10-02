# lists and list comprehension
#lists are mutable 
nums = [1, 2, 3, 4, 5]
print(nums)
#slice [starting index : ending index] .pop(5) to remove an index
# nums.append(6)
# print(nums)
# nums.pop(4)
# print(nums)

# for num in nums:
#     print(num)

# nums_squared = []

# nums_squared = [num * num for num in nums]
# print(nums_squared)

# nums_cubed = []

# nums_cubed = [num ** 3 for num in nums if num % 2 == 0]
# print(nums_cubed)

# for num in nums: 
#     if num % 2 == 0:
#         nums_cubed.append(num * num * num)
# dictionaries
    #dictionaries are mutable 

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squares [6] = 36
print(squares)
# sets
    #no duplicates in a set. sets are mutable 

plants = set()

plants.add("tree")
plants.add("bush")
plants.add("flower")

print(plants)

# tuples
    # are immuatble. 
color = (9, 18, 200)
print(color)