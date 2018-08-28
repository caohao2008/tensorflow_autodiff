import sys
import os
from op import *
from expr import *

class Executor:
	def __init__(self):
		print "init executor"
	
	def buildComputation(self,expr_table):
		backward_op_table = {}
		forward_input_table = {}
		forward_op_table = {}
		for expr in expr_table:
			print expr
			forward_op_table[str(expr.output)]=expr.operator().forward
			forward_input_table[str(expr.output)]=expr.inputs
			index = 0
			for input in expr.inputs:
				backward_op_table[str(expr.output)+","+input]=expr.operator().backward(input,index,expr.inputs)
				index=index+1
		print forward_op_table
		print forward_input_table
		print "backward op table ",backward_op_table
		return forward_op_table,forward_input_table,backward_op_table
	
	def execute(self,forward_op_table,forward_input_table,_input_values):
		input_values = _input_values
		value_table  = {}
		##fill in input value
		#find_values(value_t
		times = 0
		while 1:
			fill_all = 1
			for key in forward_op_table:
				cur_input = forward_input_table[key]	
				cur_values = []
				skip_value = 0
				for input in cur_input:
					print "execute for key "+key
					if(_input_values.has_key(input)):
						cur_values.append(_input_values[input])
					elif(value_table.has_key(input)):
						cur_values.append(value_table[input])
					else:
						skip_value = 1
				if skip_value!=1:		
					value_table[key]=forward_op_table[key](cur_values)
				else:
					fill_all = 0
			print "value_table = ",value_table
			if(fill_all>0):
				break
		
		print "value_table = ",value_table
		return value_table
	
	def executeStep(self,op,inputs,_values,new_value):
		print inputs
		print _values
		_inputs = []
		for i in inputs:
			if type(i) == str:
				if i=="y":
					_inputs.append(_values[i])
				else:
					if(new_value.has_key(i)):
						##using as param, use new value
						_inputs.append(new_value[i])
					else:
						_inputs.append(_values[i])
			elif isinstance(i,Expr):
				print "Expr! Expr=",i
				_inputs.append(self.executeStep(i.operator,i.inputs,_values,new_value))
			else:
				_inputs.append(i)
		print "op ="+str(op)+" inputs="+str(_inputs)
		if type(op)==int:
			return op
		elif type(op)==str:
			##use as op, should use origin value
			return _values[op]
		else:
			return op().forward(_inputs)

			
	def executeBackward(self,backward_queue,backward_expr_table,_input_values):
		new_value_table={}
		while not backward_queue.empty():
			cur_node = backward_queue.get()	
			print cur_node
			print backward_expr_table[cur_node]
			expr = backward_expr_table[cur_node]
			cur_inputs = []
			for sub in expr.inputs:
				if(isinstance(sub,Expr)):
					result = self.executeStep(sub.operator,sub.inputs,_input_values,new_value_table)
					cur_inputs.append(result)
				else:
					cur_inputs.append(sub)
			print "params ", cur_inputs
			result = self.executeStep(expr.operator,cur_inputs,_input_values,new_value_table)
			new_value_table[cur_node]=result
			print new_value_table
			print "execute"	
