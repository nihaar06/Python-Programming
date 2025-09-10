def students(l):
    max_student=max(l,key=lambda x:x[2])
    print("The student with maximum marks is: ",max_student[1])
    print("Names of students who scored more than 75 marks are: ")
    for i in l:
        if i[2]>=75:
            print(i[1])
l=[(520, "John", 78), (521, "Jane", 52), (522, "Doe", 90), (523, "Alice", 45), (524, "Bob", 88)]
students(l)