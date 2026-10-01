# __init__ is a special method that Python calls automatically when you create an object.

# Set up the newly created object's initial state.


class Student:
    def __init__(self, name):
        self.name = name

student = Student("Dev")


""" 
Student("Dev", 21, "ML")

          self
           ↓
      +-----------+
      | Student   |
      |-----------|
      | name      | → "Dev"
      | age       | → 21
      | course    | → "ML"
      +-----------+

"""
