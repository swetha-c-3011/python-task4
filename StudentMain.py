from Student import School, Student,AdvancedSchool
import traceback


class SchoolMain:

    # def __init__(self,id,name):
    #     self.id=id
    #     self.name=name
    #     self.studentObj=Student(self.id,self.name)
    #     self.schoolObj=School(self.studentObj)


    def implement_switch(self):

        try:
            while True:
                num=input("\nPress 1 To  add student"
                          "\nPress 2 To remove student"
                          "\nPress 3 To search Student"
                          "\npress 4 To use generator"
                          "\npress 5 To find students whose avg is higher than given input"
                          "\npress 6 To exit")
                match num:
                    case "1":
                        newname = input("enter your name").strip().lower()
                        try:
                            newid = int(input("enter your id"))
                            if  newid<0:
                                raise ValueError("ID must be a >0 and Id should be of type int.")
                            # print("Here")
                            # for d in Student.collection_of_dict:
                            #     print(type(d))

                            # if not any (d['student_id']==id for d in Student.collection_of_dict):
                            StudentObj = Student(newid, newname)
                            SchoolObj = School(StudentObj)
                            if any(d['student_id'] == newid for d in School.collection_of_dict):
                                print(f"id {newid} is already taken")
                            else:
                                num = int(input("number of marks to be added"))
                                SchoolObj.addmarks(num,newid)
                        except ValueError as val_err:
                            print(f"ValueError occurred:ID should be a numeric value")
                        except Exception as e:
                            print(f"An error occurred while adding a student: {e}")

                    case "2":
                        try:
                            if not School.collection_of_dict:
                                print("Students list is empty,Try adding students and try again")
                            else:
                                id = int(input("enter the id of the student to removed"))
                                if id<0:
                                    raise ValueError("ID must be a number and Id should be of type int.")
                                SchoolObj.removeStudent(id)
                        except ValueError as val_err:
                            print(f"ValueError occurred: ID should be a numeric value")
                        except Exception as e:
                            print(f"An error occurred while adding a student: {e}")

                    case "3":
                        try:
                            if not School.collection_of_dict:
                                print("Students list is empty,Try adding students and try again")
                            else:
                                id=int(input("enter the id of the student to search"))
                                if  id<0 :
                                    raise ValueError("ID must be a number and and Id should be of type int.")
                                SchoolObj.searchStudent(id)
                        except ValueError as val_err:
                            print(f"ValueError occurred: ID should be a numeric value")
                        except Exception as e:
                            print(f"An error occurred while adding a student: {e}")
                            print(traceback.format_exc())

                    case "4":
                        try:
                            if not School.collection_of_dict:
                                print("Students list is empty,Try adding students and try again")
                            else:
                                SchoolObj.__iter__()
                                for student in SchoolObj:
                                    print("printing from iterator : ", student)
                        except TypeError as type_err:
                            print(f"TypeError occurred: {type_err}")
                        except Exception as e:
                            print(f"An error occurred while using the iterator: {e}")
                    case "5":
                        try:
                            if not School.collection_of_dict:
                                print("Students list is empty,Try adding students and try again")
                            else:
                                avg=float(input("enter the average"))
                                if 100<avg < 0:
                                    raise ValueError("Average must be a number.")

                                AdvancedObj = AdvancedSchool(StudentObj)
                                AdvancedObj.find_students_above(avg)


                        except ValueError as val_err:
                            print(f"ValueError occurred: average value should be a interger or float")
                        except Exception as e:
                            print(f"An error occurred while adding a student: {e}")
                    case "6":
                        print("program exit")
                        break
                    case _:
                        print("provide a value input between 1 - 6")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
# name=input("enter the name").lower().strip()
# id=int(input("enter id"))
SchoolMainObj=SchoolMain()
    # SchoolMainObj=SchoolMain(id,name)
SchoolMainObj.implement_switch()












