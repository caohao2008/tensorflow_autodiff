import sys
import os
import math

class Op:
	def forward(self,_inputs):
		print "forward"
		return "basic forward op"
	
	def backward(self,_inputs):
		print "backward"
		return "basic backward op"
		

class Assign:
	def forward(self,_inputs):
		print "forward assign",_inputs
		return _inputs[0]
	
	def backward(self,_inputs):
		print "backward assign"
		return "backward assign"

class Plus(Op):
	def forward(self,_inputs):
                print "forward plus"
		return _inputs[0]+_inputs[1]
	
	def backward(self,_inputs):
		print "backward plus"
 
class Minus(Op):
	def forward(self,_inputs):
                print "forward minus"
		return _inputs[0]-_inputs[1]
                return "forward minus",_inputs
	
	def backward(self,_inputs):
		print "backward minus"
 
class Mult(Op):
	def forward(self,_inputs):
                print "forward mult"
		return _inputs[0]*_inputs[1]
		return "forward mult",_inputs
	
	def backward(self,_inputs):
		print "backward mult"


 
class Sin(Op):
	def forward(self,_inputs):
                print "forward sin"
		return math.sin(_inputs[0])
		return "forward sin",_inputs
	
	def backward(self,_inputs):
		print "backward sin"

 
class Ln(Op):
	def forward(self,_inputs):
                print "forward ln"
		return math.log(_inputs[0])
		#return "forward ln",_inputs
	
	def backward(self,_inputs):
		print "backward ln"

 
