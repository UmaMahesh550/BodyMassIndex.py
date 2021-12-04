'''Body Mass Index Problem'''
'''Input of Weight and Height from the user'''
import abc
class Bmi(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def calculation(self):
		pass
	@abc.abstractmethod
	def prediction(self):
		pass

class BodyMassIndex(Bmi):
	def __init__(self):
		self.weight=float(input("Please provide us your Weight(kg) : "))
		self.height=float(input("Please provide us your Height(cm or m) : "))
		self.unit=int(input("'1' : Kilograms,Centimeters\n'2' : Kilograms,Metres)\n'3' : Pounds,Inches\nUNIT : "))

	'''BMI Calculation part'''
	def calculation(self):
		if(self.unit==1):
			self.bmi=(self.weight/self.height/self.height)*10000
		elif(self.unit==2):
			self.bmi= self.weight/(self.height)**2
		elif(self.unit==3):
			self.bmi=(self.weight/(self.height)**2)*703
		else:
			print("Invalid Unit.")

	'''Health Prediction'''
	def prediction(self):
		print("Your Body Mass Index is : {} kg/m^2".format(self.bmi))
		if self.bmi<18.5:
			print("You are underweight, should consult a nutrition doctor.")
		elif self.bmi>=18.5 and self.bmi<=24.9:
			print("You are Normal and Healthy.")
		elif self.bmi>24.9 and self.bmi<30:
			print("Oh god! You are Overweight, should have some diet plan introduced.")
		else:
			print("You are Obese should consult a nutrition doctor.")
		print("Leading Healthy Life is more important to have a Healthy Heart so maintain a Healthy Life")

class Main():
	obj=BodyMassIndex()
	obj.calculation()
	obj.prediction()
