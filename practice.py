#print sum of first 10 even numbers
list = [1,2,3,4,5,6,7,8,9,0,2,5,4,6,7,8,3,0,4,8]
count = 0
sum = 0
for i in list:
    if i%2==0:
        sum = sum + i
        count = count + 1

        if count == 10:
            break
print("Sum of first 10 even numbers: ", sum)
        
#Accept 2 values S and N Print square of first N numbers starting from S
#Reverse the accepted string
#Accept sentence from user and count the vowels
#Remove duplicates from list
#Reverse the list 
