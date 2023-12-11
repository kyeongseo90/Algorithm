#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool isGoodWord() {
	stack<char> good;
	string tmp;
	getline(cin, tmp);
	for (int i = 0; i < tmp.size(); i++) {
		if (good.empty() || tmp[i] != good.top())
			good.push(tmp[i]);
		else
			good.pop();
	}
	if (good.empty()) return true;
	else return false;
}
int main() {
	int N;
	cin >> N;
	cin.ignore();
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		if (isGoodWord()) cnt++;
	}
	cout << cnt;
}