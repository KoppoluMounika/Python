class Student:
    school_name="Central High School"
    def __init__(self,name):
        self.name=name
        
    
s1=Student("ram")
s2=Student("mounika")
print(s1.school_name)
print(s2.school_name)