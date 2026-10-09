#create dictionary with student details
students = {
    101: {"Name": "Aditi", "Scores": [20,20,25]},
    102: {"Name": "Rahul", "Scores": [45,60,50]},
    103: {"Name": "Sneha", "Scores": [0,14,95]},
    104: {"Name": "Karan", "Scores": [55,12,43]},
    105: {"Name": "Priya", "Scores": [49,51,47,33]}
}
#Calculate avg score and flag pass/fail
for sid, details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"]) #avg using sum and len
    details["Average"] = avg
    details["Passed"] = avg >=30 #boolean flag

#print names of students who passed
print("Students who passed: ")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])