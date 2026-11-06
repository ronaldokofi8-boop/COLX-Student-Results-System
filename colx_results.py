print("......WELCOME STUDENTS......")
student1 = input("enter ur name: ")
score1 = int(input("enter ur scores: "))
score2 = int(input("enter ur scores: "))
score3 = int(input("enter ur scores: "))
score4 = int(input("enter ur scores: "))
total_score = 0 
total = score1 + score2 + score3 + score4
total1 = total
avg = total1 / 4
print("......STUDENT1 RESULTS......")
print("student: ", student1)
print("total score: ", total1)
print("average score: ", avg)
if avg >=80:
    print("excellent")
elif avg >=70:
    print("good work")
elif avg >=60:
    print("you pass")
else:
    print("you failed")


student2 = input("enter ur name: ")
score1 = int(input("enter ur scores: "))
score2 = int(input("enter ur scores: "))
score3 = int(input("enter ur scores: "))
score4 = int(input("enter ur scores: "))
total_score = 0 
total = score1 + score2 + score3 + score4
total2 = total
avg2 = total2 / 4
print("......STUDENT2 RESULTS......")
print("student: ", student2)
print("total score: ", total2)
print("average score: ", avg2)
if avg2 >=80:
    print("excellent")
elif avg2 >=70:
    print("good work")
elif avg2 >=60:
    print("you pass")
else:
    print("you failed")




student3 = input("enter ur name: ")
score1 = int(input("enter ur scores: "))
score2 = int(input("enter ur scores: "))
score3 = int(input("enter ur scores: "))
score4 = int(input("enter ur scores: "))
total_score = 0 
total = score1 + score2 + score3 + score4
total3 = total
avg3 = total3 / 4
print("......STUDENT3 RESULTS......")
print("student: ", student3)
print("total score: ", total3)
print("average score: ", avg3)
if avg3 >=80:
    print("excellent")
elif avg3 >=70:
    print("good work")
elif avg3 >=60:
    print("you pass")
else:
    print("you failed")

print("......CLASS RESULTS......")
class_average = (avg + avg2 + avg3) / 3
print("class average: ", class_average)
hightest_average = max(avg, avg2, avg3)
print("highest average: ", hightest_average)

if hightest_average == avg :
    print("Top student:", student1)
elif hightest_average == avg2:
    print("Top student:", student2)
else:
    print("Top student:", student3)

print("......THANK YOU......")
