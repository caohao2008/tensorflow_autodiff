import sys
import os

class Op:
	def forward(self,*_inputs):
		print "forward"
	
	def backward(self,*_inputs):
		print "backward"

class Assign:
	def forward(self,*_inputs):
		print "forward assign"
	
	def backward(self,*_inputs):
		print "backward assign"



class Plus(Op):
	def forward(self,*_inputs):
                print "forward plus"
	
	def backward(self,*_inputs):
		print "backward plus"
 
class Minus(Op):
	def forward(self,*_inputs):
                print "forward minus"
	
	def backward(self,*_inputs):
		print "backward minus"
 
class Mult(Op):
	def forward(self,*_inputs):
                print "forward mult"
	
	def backward(self,*_inputs):
		print "backward mult"


 
class Sin(Op):
	def forward(self,*_inputs):
                print "forward sin"
	
	def backward(self,*_inputs):
		print "backward sin"

 
class Ln(Op):
	def forward(self,*_inputs):
                print "forward ln"
	
	def backward(self,*_inputs):
		print "backward ln"

 
