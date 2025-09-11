class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name:",self.name,"\nSalary:",self.salary)
class Manager(employee):
    def __init__(self, name, salary,dept):
        super().__init__(name, salary)
        self.dept=dept
    def display(self):
        super().display()
        print("Department:",self.dept)
emp=employee('Rak',40000) 
emp.display()
e2=Manager('Kiran',60000,'R&D')
e2.display()