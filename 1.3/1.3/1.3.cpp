// 1.3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<unordered_set>
#include<string>
#include<algorithm>

using namespace std;

//1. sort and then remove adjust same character.  = O(nlogn) + O(n)
void removeDuplicate1(char str[],int n)
{
	sort(str,str+n);
	cout << str << endl;
	//for (int i = 0; i < n; ++i)
	//{
	//	if (str[i] == str[i + 1]);
	//}



}

int main()
{
	string str = "Himanshu Negi";
	int size = sizeof(str) / sizeof(str[0]);
	removeDuplicate1(&str[0],size);
    return 0;
}

