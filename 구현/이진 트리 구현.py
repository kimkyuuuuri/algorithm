class Node:
        def __init__(self, data):
                self.data=data
                self.left_node=None
                self.right_node=None
        def right(self,rightnode):
                
                self.right_node.data=rightnode
        def left(self, leftnode):
                
                self.left_node.data=leftnode

        def add2(self,data)->bool:
                def add_node(node,data)->None:
                       
                        if self.data > data:
          
                                if self.left_node is None:
                                        self.left_node = data
                                else:
         
                                        add_node(self.left_node,data)
        
                        else:
                                if self.right_node is None:
                                        self.right_node = data
                                else:
                                        add_node(self.right_node,data)
            
            
   
        def add(self,node,data):
              
                if data.data < node.data:
                        if node.left_node is None:
                                self.left_node=data
                                self.left(data.data)
                        else:
                               
                                self.add(node.left_node,data)
                                
                else:
                        if node.right_node is None:
                                self.right_node=Node(data)
                                self.right(data.data)
                        else:
                                self.add(node.right_node,data)
                return True
                
                

       
                    

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
                post_order(tree[node.left_node.data])
        if node.right_node != None:
                post_order(tree[node.right_node.data])
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
        print(num[i])
        tree[num[i]]=Node(num[i])
        tree[num[0]].add(tree[num[0]],tree[num[i]])
        
print(tree[num[0]].left_node)

post_order(tree[num[0]])
