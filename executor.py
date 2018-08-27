import sys
import os
from op import *

class Executor:
	def __init__(self):
		print "init executor"
	
	def buildComputation(self,expr_table):
		backward_table = {}
		forward_table = {}
		for expr in expr_table:
			print expr
			forward_table[str(expr.output)]=expr.operator().forward
			for input in expr.inputs:
				backward_table[str(expr.output)+","+input]=expr.operator().backward
		print forward_table
		print backward_table
		return forward_table,backward_table
	
	def execute(self,forward_table,*_input_values):
		input_values = _input_values
		value_table  = {}
		for key in forward_table:
			value_table[key]=forward_table[key](_input_values)
		print value_table
		return value_table
	
							
