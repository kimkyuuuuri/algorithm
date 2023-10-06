#include<iostream>
using namespace std;

int main(int argc, char** argv)
{

	int a,b;
	cin>>a>>b;
	int array1[a][2]={};
	int array2[b][2]={};

	for (int i=0; i<a; i++){
		int temp1, temp2;
		cin>>temp1>>temp2;
		if (i!=0){
			array1[i][0]=array1[i-1][0]+temp1;
		}
		else{
			array1[i][0]=temp1;
		}
		array1[i][1]=temp2;
	}

	int index=0;
	int temp_answer=0;
	for (int i=0; i<b; i++){
		int temp1, temp2;
		cin>>temp1>>temp2;
		if (i!=0){
			array2[i][0]=array2[i-1][0]+temp1;
		}
		else{
			array2[i][0]=temp1;
		}
		array2[i][1]=temp2;
		
		while ( index < a-1 && array2[i][0]>array1[index][0] && array2[i][0]<=array1[index+1][0]){
			index+=1;
		}
		
		temp_answer=max(temp_answer, array2[i][1] - array1[index][1]);
		
	}
	cout<<temp_answer;

	return 0;
}
