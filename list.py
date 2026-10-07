#empty list
my_list = []
print(my_list)

#with items
fruits = ["apple", "banana", "cherry"]
print(fruits)

#to access list elts using index
#positive indicate from start negative indicates from end 
nums = [10, 20, 30, 40]
print(nums[0])
print(nums[-1])

#append item in list
colors = ["red", "blue"]
colors.append("green")
print("After adding at last: ", colors)

#Functions
#Length
numbers = [1,2,3,4,5,7,5,9]
print("No. of items in list are: ", len(numbers))

#Sum
print("Sum of the list numbers is: ", sum(numbers))

#sorting
print("List is in Ascending order: ", sorted(numbers)) #by default ascending
print("List in decending order: ", sorted(numbers, reverse=True))