#create a list of 10 no. and display the sum of last 4 elts
list = [1,4,5,2,8,3,6,8,2,3]
print("Sum of last 4 elements: ", sum(list[-4:]))

#remove the items from the list located at 2nd and 5th position
list.pop(4)
list.pop(1)
print("Aftering removing 2nd and 5th elt: ", list)

#print the diff btwn highest and smallest of the list 
diff = max(list) - min(list)
print("Difference between max and min of the list: ", diff)

#append a new elt in a list which is half of the item of 3rd position 
list.append(list[2]//2)
print("After appending:", list)
