class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is (self.name) and I am (self.age) year old")

class student(person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def introduce(self):
        super().introduce()
        print(f"My student ID is {self.student_id}")
person1 = person("Jhon",30)
person1.introduce()
student1 = student("Mary",20,"12345")
student1.introduce()