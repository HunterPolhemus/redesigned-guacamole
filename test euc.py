# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:42:20 2017

@author: Huntrer
"""


import math as m

# student.py
#
# Defines a class to represent information for an individual student.

class Student :
   "Represents an individual student."
   def __init__(self, gender = 0, classStanding = 0,
                 firstName = "", lastName = "", 
                 gpa = 0.0) :
      self.gender = gender
      self.classStanding = classStanding
      self.firstName = firstName
      self.lastName = lastName
      self.gpa = gpa

   def getClass() :
        """Returns the string representation for the student's
           classification code."""

if classStanding == 0   :
          return "Freshman"
elif classStanding == 1 :
         return "Sophomore"
elif classStanding == 2 :
         return "Junior"
elif classStanding == 3 :
         return "Senior"

def getName( reversed ) :
        """Returns the student's name in one or two formats:
           'first last' if reversed is false or 'last first'
           if reversed is true."""

if reversed == False :
         return self.firstName + " " + self.lastName
else :
         return self.lastName + " " + self.firstName
def gender( ):