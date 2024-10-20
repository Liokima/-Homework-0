#Средний бал

Grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
Students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

S1 = (sum(Grades[0]) / len(Grades[0]))
Grades[0] = S1

S2 = (sum(Grades[1]) / len(Grades[1]))
Grades[1] = S2

S3 = (sum(Grades[2]) / len(Grades[2]))
Grades[2] = S3

S4 = (sum(Grades[3]) / len(Grades[3]))
Grades[3] = S4

S5 = (sum(Grades[4]) / len(Grades[4]))
Grades[4] = S5

list_student = list(Students)[:5]
list_student.sort()

All_Set = {list_student[0]:Grades[0],list_student[1]:Grades[1],list_student[2]:Grades[2],list_student[3]:Grades[3],list_student[4]:Grades[4]}
print(All_Set)


