# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:47:46 2017

@author: Huntrer
"""

import math as m
import numpy as np 

# ----------------------------------------------------------------------------- 
# Question 1 
# ----------------------------------------------------------------------------- 
class Student(object):
    """This is the student class. """

    def __init__(self, firstname = 'Student', lastname = 'Student', 
                 gender = 'Male or Female', status = 'Freshman, Sophomore, Junior, Senior', gpa = 0.0):
        """Initialize the student-object with a
        default name variable"""
        self.firstname = firstname 
        self.lastname = lastname
        self.gender = gender
        self.status = status 
        self.gpa = gpa  

    def showMyself(self):
        """Method: showMyself()
        prints out all the variables."""
        print("\n")
        print("Hello, let me introduce myself.")
        print("-------------------------------")
        print("My first name is {}".format(self.firstname))
        print("My last name is {}".format(self.lastname))
        print("My gender is {}".format(self.gender))
        print("My status is {}".format(self.status))
        print("My gpa is {}".format(self.gpa))
        print("-------------------------------\n")

    def studyTime(self, study_time):
        """Method: studyTime increments student GPA according to the following
        formula: gpa = gpa + log(study_time)"""
        self.gpa = gpa + np.log(study_time)

# ----------------------------------------------------------------------------- 
# Question 2 
# ----------------------------------------------------------------------------- 
StudentList = []
firstname_list = ['Mike', 'Jim', 'Jack', 'Jane', 'Mary']
lastname_list = ['Barnes', 'Nickerson', 'Indabox', 'Miller', 'Scott']
gender_list = ['Male', 'Male', 'Male', 'Female', 'Female']
status_list = ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Senior']

gpa_list = [4.0, 3.0, 2.5, 3.6, 2.7]

for i, (firstname, lastname, gender, status, gpa,) in enumerate(zip(firstname_list, lastname_list, gender_list, status_list, gpa_list)):
    StudentList.append(Student(firstname=firstname, lastname=lastname, gender=gender, status=status, gpa=gpa))
print(StudentList)

StudentList[0].showMyself()
StudentList[1].showMyself()
StudentList[2].showMyself()
StudentList[3].showMyself()
StudentList[4].showMyself()


# ----------------------------------------------------------------------------- 
# Question 3 
# ----------------------------------------------------------------------------- 
StudentList[0].studyTime(study_time=60)
StudentList[1].studyTime(study_time=100)
StudentList[2].studyTime(study_time=40)
StudentList[3].studyTime(study_time=300)
StudentList[4].studyTime(study_time=1000)

StudentList[0].showMyself()
StudentList[1].showMyself()
StudentList[2].showMyself()
StudentList[3].showMyself()
StudentList[4].showMyself()
        