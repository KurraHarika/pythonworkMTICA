student=[[44,'Prasad',75,87],[13,'Gangully',82,79],[43,'Pradeep',80,85],[17,'Harika',79,80]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
