# class celsius:
#   def __init__(self,temperature):
#     self.__temperature=temperature

#   def get_temp(self):
#     return self.__temperature
#   def set_temp(self,text):
#     if text<=100 and text>=0:
#       self.__temperature=text
#     else:
#       raise Exception("შეიყვანე 0 იდან  100 ის ჩათ ვლით რიცხვები")

#   temp=property(get_temp,set_temp)

# obj1=celsius(30)
# print(obj1.temp)
# obj1.temp=101
# print(obj1.temp)


# class people:
#   def __init__(self,firstname,lastname,age):
#     self.firstname=firstname
#     self.lastname=lastname
#     self.age=age

#   def fullname(self):
#     return self.firstname+" "+self.lastname

#   def email(self):
#     return self.firstname+"."+self.lastname+"@gmail.com"


# class lecturer(people):
#   def __init__(self,firstname,lastname,age,salary):
#     super().__init__(firstname,lastname,age)
#     self.__salary=salary

#   def get_salary(self):
#     return self.__salary
#   def set_salary(self,new_salary):
#     self.__salary=new_salary

#   salar=property(get_salary,set_salary)

# class student(people):
#   def __init__(self,firstname,lastname,age,courses,grades):
#     super().__init__(firstname,lastname,age)
#     self.grades=grades
#     self.courses=courses


#   def get_average_grade(self):
#     shekreba=sum(self.grades)
#     amount=len(self.grades)
#     return shekreba/amount


# student1=student("teona","porchkhidze",19,"technology",[100,100,80])
# print(student1.email())
# print(student1.fullname())
# print(student1.grades)
# print(student1.get_average_grade())
# print(student1.courses)


# lecturer1=lecturer("giorgi","giorgadze",45,1000)
# print(lecturer1.salar)
# print(lecturer1.fullname())
# print(lecturer1.email())
#
#
# class people:
#     def __init__(self,name):
#         self.name=name
# class instructor(people):
#     def __init__(self,name,salary):
#         people.__init__(self,name)
#         self.salary=salary
#
# class student(people):
#     def __init__(self,name,grades):
#         people.__init__(self,name)
#         self.grades=grades
# class doc_student(student,instructor):
#     def __init__(self,name,grades,salary):
#         student.__init__(self,name,grades)
#         instructor.__init__(self,salary)
#
# name="teona"
# grades=[1,2,3]
# salary=5
#
# obj1=doc_student(name,grades,salary)
#
# print(doc_student.mro())


class currency:
    lari={"USD":1/2,"EURO":1/4}
    def __init__(self,value,unit="GEL"):
        self.value=value
        self.unit=unit

    def __str__(self):
        return str(self.value/1)+" "+self.unit

    def ChangeTo(self,valuta):
        for k,v in currency.lari.items():
          if k==valuta:
            return self.value*v
          else:
            pass


    def __add__(self,other):
        if isinstance(other,currency):
          if other.unit==self.unit:
            summa=self.value+other.value
          else:
            summa=self.value+other.ChangeTo(other.unit)
        else:
          summa=self.value+other
        return summa

    def __mul__(self,other):
        try:
          return self.value*other
        except TypeError :
          print("გამრავლება სრულდება რიცხვებზე")


    f1=currency(500)
    f2=currency(200,"EURO")
    print(f1.__add__(90))
    print(f1.ChangeTo("EURO"))
    print(f1.__add__(f2))
    print(f1*5)
    print(5*f1)


