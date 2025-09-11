class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("Name: ",self.name,"\nRoll no.: ",self.roll_no,'\nMarks: ',self.marks)
s1=Student('Rakesh',543,78)
s2=Student('Kiran',523,89)
s1.display()
s2.display()