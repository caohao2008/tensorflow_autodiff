import sys
import os

class Expr:
	def __init__(self,_output,_op,* _inputs):
		self.output = _output
		self.operator = _op
		self.inputs = _inputs
		print "init express"	


	def __str__(self):
		expr = ""
		expr= expr+str(self.operator)+"("
		for input in self.inputs:
			#print type(input)
			if(isinstance(input,Expr)):
				expr = expr + str(input) + ","
			else:
				expr =  expr + input+","
		expr = expr[:-1]+")"
		result = str(self.output)+" = "+expr
		return result 
