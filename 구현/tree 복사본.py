class Node:
        def __init__(self, data):
                self.data=data
                self.left_node=None
                self.right_node=None
        def right(self,rightnode):
                
                self.right_node=rightnode
        def left(self, leftnode):
                
                self.left_node=leftnode

       
                    

# 전위 순회
def pre_order(node):
        print(node.data, end='')
        if node.left_node!= None:
                pre_order(tree[node.left_node])

        if node.right_node!= None:
                pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
        if node.left_node != None:
                in_order(tree[node.left_node])
        print(node.data, end='')
        if node.right_node != None:
                in_order(tree[node.right_node])

# 후위 순회
def post_order(node):
        
        if node.left_node != None:
                post_order(tree[node.left_node])
        if node.right_node != None:
                post_order(tree[node.right_node])
        print(node.data, end='\n')


tree = {}
num=[]
# data.. 출력 넣기 ..
while True:
    try:
        num.append(int(input()))
    except:
        break

#문제 작을 때 하나의 케이스만 본다고 ㄱ되는게 아

tree[num[0]]=Node(num[0])
for i in range(1,len(num)):
        index=0
        
        if num[i-1]>num[i]:
                for j in range(i-1,-1,-1):
                        
                        if tree[num[j]].data > num[i]:
                               
                                index=j
                        else:
                                break
                
                tree[num[i]]=Node(num[i])
                tree[num[index]].left(num[i])
           
              
        else:
                for j in range(i-1,-1,-1):
                        
                        if tree[num[j]].data < num[i]:
                               
                                index=j
                        else:
                                break
                        
                              
       
        
                tree[num[i]]=Node(num[i])
                
                tree[num[index]].right(num[i])
                


post_order(tree[num[0]])
