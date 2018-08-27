import sys
import os

class Op:
	def forward(self):
		print "forward"
	
	def backward(self):
		print "backward"

class plus(Op):
	def forward(self):
                print "forward plus"
	
	def backward(self):
		print "backward plus"

 
