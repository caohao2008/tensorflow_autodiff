import sys
import os

class Op:
	def forward(self):
		print "forward"
	
	def backward(self):
		print "backward"

class Assign:
	def forward(self):
		print "forward assign"
	
	def backward(self):
		print "backward assign"



class Plus(Op):
	def forward(self):
                print "forward plus"
	
	def backward(self):
		print "backward plus"
 
class Minus(Op):
	def forward(self):
                print "forward minus"
	
	def backward(self):
		print "backward minus"
 
class Mult(Op):
	def forward(self):
                print "forward mult"
	
	def backward(self):
		print "backward mult"


 
class Sin(Op):
	def forward(self):
                print "forward sin"
	
	def backward(self):
		print "backward sin"

 
class Ln(Op):
	def forward(self):
                print "forward ln"
	
	def backward(self):
		print "backward ln"

 
