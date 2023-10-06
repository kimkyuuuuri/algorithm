#include<iostream>
#include <string>


using namespace std;

int main(int argc, char** argv)
{

	int n,m ;
	cin>>n>>m;
	//char array1[n][10];
	string array1[n]={};
	//string time[n]
	int time[n][19];

	// 이제 각 번호대로 이름이 부여된 것 
	for(int i=0; i<n; i++){
		cin>>array1[i];
	}

	for (int i = 0; i < n; i++) {
        for (int j = 0; j < 18; j++) {
            time[i][j] = 0;
        }
    }


	// 딕셔너리도 같은 원리니까 상관 없을까?
	for (int i=0; i<m+1; i++){
		// 하나씩 돌면서 맞는지 확인하기
		string temp;
		int start,end;
		cin>>temp>>start>>end;
		for (int j=0; j<n; j++){
			
			if (array1[j].compare(temp) == 0){
				for (int k=start; k<end; k++){
				time[j][k]=1;
				break;
				}

			}
		}
	}


	for (int i=0; i<n; i++){
		char temp[18];
		int flag=0;
		cout<<"------";
		for (int j=9; j<19; j++){
			// 0이면 저장 
			if (time[i][j]==0 && flag==0){
				cout<<j;
				flag=1;
			}
			else if (time[i][j]==1 && flag==1){
				cout<<"-" <<j<<"\n";
				flag=0;
			}
			else if (time[i][j]==0 && flag==1){
				continue;
			}
		
		}
	}
	
	return 0;
}
