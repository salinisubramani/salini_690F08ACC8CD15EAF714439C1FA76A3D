class Student:
    def __init__(self,name,roll_number,cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa

    def sort_student(student_list):
        sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)

        #syntax-lambda arg:rxp
        return sorted_students


Students=[ 
           Student("gowtham","A124",9.8),
           Student("srikanth","A125",8.9),
           Student("mahidhar","A126",9.2)
      ]
sorted_Students=sort_student(Students)

for student in sorted_Students:
    print("Name:{},Roll Number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
