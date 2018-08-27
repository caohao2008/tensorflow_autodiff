import sys
import os

class Expr:
	
	def __init__(self,_output,_op,* _inputs):
		self.output = _output
		self.operator = _op
		self.inputs = _inputs
		print "init express"	
 
