TensorFlow自动求导原理

以"Automatic Differentiation in Machine Learning: a Survey"文章中的例子为例。

算法伪代码
backward，找到结束的输出节点O
建立一个先进先出队列Queue
将输出节点放入队列：Queue=[]
将与O连接的点加入队列：Queue+=neigbor(O)
Grad_Map=[]
Grad_Map[head]=y
while(队列非空，未处理完）：
Cur_Node = Queue.pop()
Add_PreNode_to_Queue(Queue,Cur_Node) （注意：如果加过就不再重复加,并且不为input）
for node in PreNode(Node):
if(Grad_Map.has_key(node)):
Grad_Map[node]=Grad_Map[node] + Hat(Cur_Node)*{ d(Cur_Node)/d(node) }
else:
Grad_Map[node]=Hat(Cur_Node)*{ d(Cur_Node)/d(node) }
if(neighbor 为input x):
Grad_Map[x]=Hat(CurNode)
推导

终点为v5。
Grad_map[v5]=y

0.
Cur_node=v5
(pop完队列是[v3])
将V5 PreNode加入队列 [v4,v3]
Grad_map[v4]=Hat(v5)* d(v5)/d(v4)
Grap_map[v3]=Hat(v5)* d(v5)/d(v3)

1.
Cur_node=v4
(pop完队列是[v3])
将V4 PreNode加入队列 [v3,v1,v2]
Grad_map[v1]=Hat(v4)* d(v4)/d(v1)
Grad_map[v2]=Hat(v4)* d(v4)/d(v2)

2.
Cur_node=v3
(pop完队列是[v1,v2])
将v3 PreNode加入队列[v1,v2,v0]
Grad_map[v0]=Hat(v3)* d(v3)/d(v0)

3.
Cur_node=v1
(pop完队列是[v2,v0])
将v1 PreNode加入队列[v2,v0,v-1]
Grad_map[v-1]=Hat(v1)* d(v1)/d(v-1)

4.
Cur_node=v2
(pop完队列是[v0,v-1])
将v2 PreNode加入队列[v0,v-1](-1和0都已经加过了)
Grad_map[v0]=Grad_map[v0]+Hat(v2)* d(v2)/d(v0)
Grad_map[v-1]=Grad_map[v-1]+Hat(v2)* d(v2)/d(v-1)


5.
Cur_node=v0
(pop完队列是[v-1])
v0的PreNode是x2，
Grad_map[x2]=Hat(v0)

5.
Cur_node=v-1
(pop完队列是[])
v-1的PreNode是x1，
Grad_map[x1]=Hat(v-1)

End
