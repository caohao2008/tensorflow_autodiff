import sys
import os
import math

class Op:
	def forward(self,_inputs):
		print "forward"
		return "basic forward op"
	
	def backward(self,_inputs,index,allinput):
		print "backward"
		return "basic backward op"
		

class Assign:
	def forward(self,_inputs):
		print "forward assign",_inputs
		return _inputs[0]
	
	def backward(self,_inputs,index,allinput):
		print "backward assign"
		return ValueOf

class ValueOf:
	def forward(self,_inputs):
		print "forward assign",_inputs
		return 1
	
	def backward(self,_inputs,index,allinput):
		print "backward assign"
		return 1


class Plus(Op):
	def forward(self,_inputs):
                print "forward plus"
		return _inputs[0]+_inputs[1]
	
	def backward(self,_inputs,index,allinput):
		print "backward plus"
		return 1
 
class Minus(Op):
	def forward(self,_inputs):
                print "forward minus"
		return _inputs[0]-_inputs[1]
                return "forward minus",_inputs
	
	def backward(self,_inputs,index,allinput):
		print "backward minus"
		if(index<1):
			return 1
		else:
			return -1
 
class Mult(Op):
	def forward(self,_inputs):
                print "forward mult"
		return _inputs[0]*_inputs[1]
		return "forward mult",_inputs
	
	def backward(self,_inputs,index,allinput):
		print "backward mult"
		if index<1:
			return allinput[1]
		else:
			return allinput[0]

 
class Sin(Op):
	def forward(self,_inputs):
                print "forward sin"
		return math.sin(_inputs[0])
		return "forward sin",_inputs
	
	def backward(self,_inputs,index,*extra):
		print "backward sin"
		return Cos
 
class Cos(Op):
	def forward(self,_inputs):
                print "forward cos"
		return math.cos(_inputs[0])
		return "forward sin",_inputs
	
	def backward(self,_inputs,index,allinput):
		print "backward sin"
		return Sin


 
class Ln(Op):
	def forward(self,_inputs):
                print "forward ln"
		return math.log(_inputs[0])
		#return "forward ln",_inputs
	
	def backward(self,_inputs,index,*allinpu):
		print "backward ln"
		return Rev

  
class Rev(Op):
	def forward(self,_inputs):
                print "forward ln"
		return 1/_inputs[0]
		#return "forward ln",_inputs
	
	def backward(self,_inputs,index,*allinput):
		print "backward ln"
		return Rev

 
