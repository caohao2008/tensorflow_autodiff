import sys
import os
import Queue
from op import *
from expr import Expr
from executor import *

#example program for tensor flow automatically differentiation
input=["x1","x2"]
node=["v-1","v0","v1","v2","v3","v4","v5"]
output=["y"]

#forward table, define forward process
forward_expr_table=[]
forward_expr_table.append(Expr("v-1",Assign,"x1"))
forward_expr_table.append(Expr("v0",Assign,"x2"))
forward_expr_table.append(Expr("v1",Ln,"v-1"))
forward_expr_table.append(Expr("v2",Mult,"v-1","v0"))
forward_expr_table.append(Expr("v3",Sin,"v0"))
forward_expr_table.append(Expr("v4",Plus,"v1","v2"))
forward_expr_table.append(Expr("v5",Minus,"v4","v3"))
forward_expr_table.append(Expr("y",Assign,"v5"))

#define graph, graph can be build from buildGraph() in tensorflow
graph=["x1:v-1","x2:v0","v-1:v1","v-1:v2","v0:v2","v0:v3","v1:v4","v2:v4","v4:v5","v3:v5","v5:y"]

###example for build graph
###def buildGraph(expr_table)
###    #implemention for buildGraph
###graph = buildGraph(forward_expr_table)

exe = Executor()
###not work , feed_dict is tensorflow based concept
###value_table = exe.execute(forward_expr_table,feed_dict={"x1":2,"x2":2,"y":3})
forward_compute_graph,forward_input_table,backward_compute_graph_table = exe.buildComputation(forward_expr_table)
value_table = exe.execute(forward_compute_graph,forward_input_table,{"x1":2,"x2":5,"y":3})

#x1=Plus(v-1,3)
#y=

node_queue = Queue.Queue()

Grad_Map={}
Grad_Map["v5"]="y"

node_queue.put("v5")
added_set=set()

##build backward graph
def find_prenode_in_graph(graph,node):
	result=[]
	for lines in graph:
		items = lines.split(":")
		start_node = items[0]
		end_node = items[1]
		if(end_node == node):
			result.append(start_node)
	return result

backward_expr_table={}
backward_expr_table["v5"]=Expr("v5",ValueOf,"y")

backward_queue = Queue.Queue() 
backward_queue.put("v5") 

while not node_queue.empty():
	cur_node = node_queue.get()
	###print cur_node
	#find pre node of cur_node
	pre_nodes = find_prenode_in_graph(graph,cur_node)
	###print pre_nodes
	
	for pre_node in pre_nodes:
		if pre_node.startswith("x"):
			Grad_Map[pre_node]="Hat("+cur_node+")"
			expr=Expr(pre_node,Assign,cur_node)
			backward_expr_table[pre_node]=expr
			continue
		expr1 = Expr("d("+cur_node+")/d("+pre_node+")",backward_compute_graph_table[cur_node+","+pre_node],pre_node)
		expr2 = Expr(pre_node,Mult,expr1,cur_node)
		if not Grad_Map.has_key(pre_node):
			Grad_Map[pre_node]="Hat("+cur_node+")* d("+cur_node+")/d("+pre_node+")"
			#backward_expr_table[pre_node]=Expr(pre_node,Mult,backward_compute_graph_table[cur_node+","+pre_node])
			backward_expr_table[pre_node]=expr2
		else:
			Grad_Map[pre_node]=Grad_Map[pre_node]+"+Hat("+cur_node+")* d("+cur_node+")/d("+pre_node+")"
			expr3 = Expr(pre_node,Plus,backward_expr_table[pre_node],expr2)
			backward_expr_table[pre_node]=expr3
		if(not pre_node in added_set):
			added_set.add(pre_node)
			node_queue.put(pre_node)
			backward_queue.put(pre_node)
	
	###print node_queue
print Grad_Map
for k,v in zip(Grad_Map.iterkeys(),Grad_Map.itervalues()):
	print k+"="+v

print "backward_expr"
for k,v in zip(backward_expr_table.iterkeys(),backward_expr_table.itervalues()):
	print k+"="+str(v)


#while not backward_queue.empty():
#	print backward_queue.get()
exe.executeBackward(backward_queue,backward_expr_table,value_table)
