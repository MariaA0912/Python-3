#define class
class Student():
  #ass a constructor with two parameters
  def __init__(self, name, year):
    #save parameters as attributes
    self.name = name
    self.year = year
    self.grades = []
  #add method that takes parameter grade
  def add_grade(self, grade):
    #verify type
    if type(grade) is Grade:
      #add to grades
      self.grades.append(grade)
    


#create three instances of the class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

#create another class
class Grade():
  #add attribute
  minimum_passing = 65
  #add constructore with 1 parameter
  def __init__(self, score):
    #take parameter and assign it to self.score
    self.score = score

#create new grade 
pieter_score = Grade (100)
#add to pieter's grade with .add_grade()
pieter.add_grade(pieter_score)
