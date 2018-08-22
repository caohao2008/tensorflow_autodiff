import sys
import os
import Queue

#example program for tensor flow automatically differentiation
input=["x1","x2"]
node=["v-1","v0","v1","v2","v3","v4","v5"]
output=["y"]

graph=["x1:v-1","x2:v0","v-1:v1","v-1:v2","v0:v2","v0:v3","v1:v4","v2:v4","v4:v5","v3:v5","v5:y"]

node_queue = Queue.Queue()

Grad_Map={}
Grad_Map["v5"]="y"
node_queue.put("v5")
added_set=set()

def find_prenode_in_graph(graph,node):
	result=[]
	for lines in graph:
		items = lines.split(":")
		start_node = items[0]
		end_node = items[1]
		if(end_node == node):
			result.append(start_node)
	return result

while not node_queue.empty():
	cur_node = node_queue.get()
	print cur_node
	#find pre node of cur_node
	pre_nodes = find_prenode_in_graph(graph,cur_node)
	print pre_nodes
	
	for pre_node in pre_nodes:
		if pre_node.startswith("x"):
			Grad_Map[pre_node]="Hat("+cur_node+")"
			continue
		if not Grad_Map.has_key(pre_node):
			Grad_Map[pre_node]="Hat("+cur_node+")* d("+cur_node+")/d("+pre_node+")"
		else:
			Grad_Map[pre_node]=Grad_Map[pre_node]+"+Hat("+cur_node+")* d("+cur_node+")/d("+pre_node+")"
		if(not pre_node in added_set):
			added_set.add(pre_node)
			node_queue.put(pre_node)
	
	print node_queue
print Grad_Map
for k,v in zip(Grad_Map.iterkeys(),Grad_Map.itervalues()):
	print k+"="+v
