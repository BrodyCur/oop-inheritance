class Person:

  def __init__(self, name):
    self.name = name

  def greeting(self):
    print(f"Hi my name is {self.name}.")


class Student(Person):

  def learn(self):
    print("I get it!")


class Instructor(Person):

  def teach(self):
    print("An object is an instance of a class.")


teacher = Instructor('Nadia')
teacher.greeting()

student = Student('Chris')
student.greeting()

teacher.teach()
student.learn()


#These don't work because the student object has no relation to the Instructor class, so it cannot call methods from that class. It only shares a relation with Instructor objects with the Person class. And vice-versa. 
student.teach()
teacher.learn()

