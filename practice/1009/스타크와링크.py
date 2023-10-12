from itertools import combinations
import sys
input=sys.stdin.readline
n=int(input())
array=[]
person_number=n//2
person_array=[]
global answer_list
answer_list=[]


for i in range(n):
    array.append(list(map(int, input().split())))

def dfs(i,person_array):
    if len(person_array)==person_number:
        team1=[]
        team2=[]
        team1_score=0
        team2_score=0
        
        for j in range(n):
            if j in person_array:
                team1.append(j)
            else:
                team2.append(j)
        
        for member1 in team1:
            for member2 in team1:
                team1_score+=array[member1][member2]

        for member1 in team2:
            for member2 in team2:
                team2_score+=array[member1][member2]

        answer_list.append(abs(team1_score-team2_score))      
        return

    for j in range(i,n):
        if j not in person_array:
            person_array.append(j)
            dfs(j,person_array)
            person_array.pop()

dfs(0, person_array)
print(min(answer_list))
