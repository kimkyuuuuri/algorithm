def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
        # 타고 타고 올라감 
    return parent[x]

def union_parent(parent,a,b):
    # 부모를 찾고
    # 더 작은 곳으로 연결한다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e = map(int,input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
    a,b = map(int, input().split())
    # 입력받고 바로 합침 
    union_parent(parent,a,b)


    

    

    
