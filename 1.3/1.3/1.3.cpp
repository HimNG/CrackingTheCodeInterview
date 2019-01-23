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

}

int main()
{
	string str = "Himanshu Negi";
	int size = sizeof(str) / sizeof(str[0]);
	removeDuplicate1(str,size);
    return 0;
}

