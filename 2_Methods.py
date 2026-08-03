# Instance Methods
class Instance():
  def __init__(self,name,id):
    self.name_=name
    self.id= id
    
  def display(self):
      print(f"Name of{self.name_} and id is {self.id}")

s1 = Instance("sujal",38)
s1.display()
# class methods
class Student:
    school_name = "Tech High"  

    
    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    @classmethod
    def display(cls):
        print(f"School name is = {cls.school_name}")

S1 = Student()
Student.change_school("SOC")
Student.display()
