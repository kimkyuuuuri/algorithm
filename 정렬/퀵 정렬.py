array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end:
        return
    
    pivot=start
    left=start+1
    right=end

    #순서가 바뀔 때 까
    while (left<=right):
        #피벗보다 큰 데이터를 찾을 때 까지
        while(left<=end and array[left]<=array[pivot]):
            left+=1
            
        #피보다 작은 데이터를 찾을 때 까지
        while (right>start and array[right] >= array[pivot]):


        if(left>right):
            array[right], array[pivot] = array[pivot], array[right]

        else:
            array[left],array[right] = array[right], array[left]

    #재귀적으로 반 나눠서 실
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

#파이썬의 장점을 살린 방식
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array)<=1:
        return array
    
    pivot=array[0] #피벗은 첫 번째 원소
    tail=array[1:] #피벗을 제외한 리스트
    left_side=[x for x in tail if x<=pivot] #분할된 왼쪽 
    right_side=[x for x in tail if x>pivot] #분할된 오른 쪽

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
    
    
        


    
        
    
