// 1.2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>

using namespace std;

void reverseString(char* str,int s)
{
	for (int i = 0; i < s / 2; ++i)
	{
		char temp = str[i];
		str[i] = str[s -1 - i - 1];
		str[s -1 - i - 1] = temp;
	}
}

int main()
{
	char myString[] = "Himanshu Negi";
	int size = sizeof(myString) / sizeof(myString[0]);
	cout << "Before: " << myString << endl;
	reverseString(myString,size);
	cout << "After: " << myString << endl;
    return 0;
}