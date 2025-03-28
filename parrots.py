class Student:
    name = 'student'
    score = 'Grade'
    def __init__(self, a, b):
        self.a = a 
        self.b = b 
    
    #def avg(self):
       # return (self.a+self.b)/2

#Student1= Student(10,20)
#print(Student1.avg())

    @classmethod

    def info(cls):
        choice = input("what would you like to know")
        if choice == "name":
            return cls.name
        elif choice == "score":
            return cls.score
        else:
            return "put name or score please"
print(Student.info())

