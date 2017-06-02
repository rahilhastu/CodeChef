#include<iostream>
#include<string.h>
using namespace std;

int main(){
	char s[500];
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
	cin>>s;
	for(int i=0;i<strlen(s);i++){
		if(s[i]=='m'){
			if((s[i-1]=='s') && (i!=0)) 
				s[i-1]='*';
			else if(s[i+1]=='s'&& (i!=strlen(s)-1))
				s[i+1]='*';
		}
	}
	int	mc=0, sc=0;
	for(int i=0;i<strlen(s);i++){
		if(s[i]=='m'){
			mc++;
		}
		else if(s[i]=='s')
			sc++;
	}
	if(mc==sc) 
		cout<<"tie\n";
	else if(mc<sc) 
		cout<<"snakes\n";
	else 
		cout<<"mongooses\n";
	}
}