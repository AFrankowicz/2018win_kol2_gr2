# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)


import json

class HighschoolData():
	def __init__(self):
		self.highschool_data_filename = "highschool_data.json"
		self.highschool_data = self.load_data_to_json()

	def load_data_to_json(self):
		highschool_data = json.load(open(self.highschool_data_filename))
		return highschool_data

	def calculate_average(self, classes):
		grade_sum = 0
		all_classes = 0
		for _, values in classes.items():
			grade_sum += values["grade"]
			all_classes += 1
		return grade_sum/all_classes

	def calculate_attendance(self, classes):
		all_attendances = 0
		for _, values in classes.items():
			all_attendances += values["attendance"]
		return all_attendances

	def get_students_averages(self):
		print("***Students Averages***")
		for student in self.highschool_data["students"]:
			print("Student: {} {}. Average grade: {}".format(student["name"], student["surname"], self.calculate_average(student["classes"])))

	def get_students_attendances(self):
		print("***Students Attendances***")
		for student in self.highschool_data["students"]:
			print("Student: {} {}. Attendances: {}".format(student["name"], student["surname"], self.calculate_attendance(student["classes"])))

	def append_classes(self, all_classes, classes):
		for classname, values in classes.items():
			if classname in all_classes.keys():
				all_classes[classname]["sum"] += values["grade"]
				all_classes[classname]["num"] += 1
			else:
				all_classes[classname] = {"sum": values["grade"], "num":1}		

	def get_classess_averages(self):
		print("***Classes Averages***")
		all_classes = {}
		for student in self.highschool_data["students"]:
			self.append_classes(all_classes, student["classes"])
		for classname, values in all_classes.items():
			print("Average from {} is {}".format(classname, values["sum"]/values["num"]))


if __name__ == "__main__":
	hd = HighschoolData()
	hd.get_students_averages()
	hd.get_students_attendances()
	hd.get_classess_averages()
