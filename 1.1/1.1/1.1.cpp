// 1.1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<bitset>
#include<string>

using namespace std;

bitset<256> bs(0);

bool uniqueCheck(string str)
{
	

}

int main()
{
	string str = "CheckForDuplicateChar";
	if (uniqueCheck(str))
	{
		 cout << "chars are unique in "  << str << endl;
	}
	else
	{
		cout << "chars are not unique in " << str << endl;
	}

    return 0;
}

