workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append([0])
print(workdays)
print("Len", len(workdays))


studentsGrade = {"Mary": 9.1, "Joe":10, "Monu": 10, "Sonu":9.9 }
studentsGradeSum = sum(studentsGrade.values())
studentsGradelen = len(studentsGrade)
studentgrademean = studentsGradeSum / studentsGradelen
print("Mean Grade", studentgrademean)

count1= 0
value =10 
for value in studentsGrade:
    if studentsGrade[value] > 9.3:
        count1 = count1 +1 
print("Student getting a grade of 10 :",count1)


username = "Python3"
print(username.lower())
listRange = list(range(1, 10, 1))

print(type(studentsGrade), type(listRange)) 
##33print(listRange)
###print(product) 
print(listRange)
print(max(listRange))
studentsGradeSum = (sum(listRange)) 
studentsGradelen = len(listRange)
print("studentsGradelen", studentsGradelen)
print("studentsGradeSum",studentsGradeSum)

print(studentsGradeSum / studentsGradelen)

### Fibonacci 
sum1 = 1
sum2 = 2 
print(sum1)
print(sum2)
for i in range(1,5):
    sum =sum1+sum2
    print(sum)
    sum1 = sum


    

