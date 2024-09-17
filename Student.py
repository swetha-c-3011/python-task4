


class Student:

    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
        self.grades=[]
        self.average=0

        self.student_dict={
            "name":self.name,
            "student_id":self.student_id
        }

    def add_grades(self,grade):
        self.grades.append(grade)

    def calculate_avegare(self):
        self.average=sum(self.grades)/(len(self.grades))
        self.student_dict.update({"grades":self.grades,"average":self.average})

    def display_student_details(self):
        print("printing values from display_student_details method ",self.student_dict)




class School:
    collection_of_dict = []
    def __init__(self,studentObj):
        self.StudentObj=studentObj



    def addmarks(self,num,id):

        if not any (d['student_id']==id for d in School.collection_of_dict):
            for i in range(num):
                mark=int(input("enter marks"))
                if(mark >0 and mark< 100):
                    self.StudentObj.add_grades(mark)
                else:
                    print("mark is invalid")
            self.StudentObj.calculate_avegare()
            self.StudentObj.display_student_details()
            School.collection_of_dict.append(self.StudentObj.student_dict)
        else:
            print("id is already there")


    def removeStudent(self,id):
        # if not School.collection_of_dict:
        #     print("Students list is empty,Try adding students and try again")
        if any(d['student_id'] == id for d in School.collection_of_dict):
            for i in range(len(School.collection_of_dict)):
                if(School.collection_of_dict[i]['student_id']== id):
                    del School.collection_of_dict[i]
                    print(f"student id {id} is removed ")
                    break
        else:
            print(f"There is no student with id {id}")

    def searchStudent(self,id):
        # if not School.collection_of_dict:
        #     print("Students list is empty,Try adding students and try again")
        if any(d['student_id'] == id for d in School.collection_of_dict):
            for i in range(len(School.collection_of_dict)):
                if(School.collection_of_dict[i]['student_id']== id):
                    print( School.collection_of_dict[i])
                    print(f"student id {id} is printed ")
                    break
        else:
            print(f"There is no student with id {id}")

    def __iter__(self):
        for student in School.collection_of_dict:
            yield student

class AdvancedSchool(School):
    def __init__(self, studentObj):
        super().__init__(studentObj)

    def find_students_above(self,avg):
        # for i in range(len(School.collection_of_dict)):
        #     if (School.collection_of_dict[i]['average'] > avg):
        #         print("printing students above avg ",School.collection_of_dict[i])
        if not School.collection_of_dict:
            print("Students list is empty,Try adding students and try again")
        else:
            for item in School.collection_of_dict:
                if item["average"]>avg:
                    print(item)


