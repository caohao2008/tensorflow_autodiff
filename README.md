TensorFlow自动求导原理

以"Automatic Differentiation in Machine Learning: a Survey"文章中的例子为例。

![autodiff](https://github.com/caohao2008/tensorflow_autodiff/blob/master/autodiff_1.png)

自动求导结果

![autodiff2](https://github.com/caohao2008/tensorflow_autodiff/blob/master/autodiff_2.png)

算法伪代码<br>
	backward，找到结束的输出节点O<br>
建立一个先进先出队列Queue<br>
将输出节点放入队列：Queue=[]<br>
将与O连接的点加入队列：Queue+=neigbor(O)<br>
Grad_Map=[]<br>
Grad_Map[head]=y<br>
while(队列非空，未处理完）：<br>
Cur_Node = Queue.pop()<br>
Add_PreNode_to_Queue(Queue,Cur_Node) （注意：如果加过就不再重复加,并且不为input）<br>
for node in PreNode(Node):<br>
if(Grad_Map.has_key(node)):<br>
Grad_Map[node]=Grad_Map[node] + Hat(Cur_Node)*{ d(Cur_Node)/d(node) }<br>
else:<br>
Grad_Map[node]=Hat(Cur_Node)*{ d(Cur_Node)/d(node) }<br>
if(neighbor 为input x):<br>
Grad_Map[x]=Hat(CurNode)<br>
<br>
推导<br>

终点为v5。<br>
Grad_map[v5]=y<br>

0.<br>
Cur_node=v5<br>
(pop完队列是[v3])<br>
将V5 PreNode加入队列 [v4,v3]<br>
Grad_map[v4]=Hat(v5)* d(v5)/d(v4)<br>
Grap_map[v3]=Hat(v5)* d(v5)/d(v3)<br>

1.
Cur_node=v4<br>
(pop完队列是[v3])<br>
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
