#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> v;
vector<int> srt;

int twobig(int x, int y) {
	srt.clear();
	srt.push_back(v[x][y]);
	srt.push_back(v[x][y + 1]);
	srt.push_back(v[x + 1][y]);
	srt.push_back(v[x + 1][y + 1]);
	sort(srt.begin(), srt.end());
	return srt[2];
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		vector<int> v1(N, 0);
		v.push_back(v1);
	}
	for (int i = 0; i < N; i++) 
		for (int j = 0; j < N; j++) 
			cin >> v[i][j];
	while (N) {
		for (int i = 0; i < N / 2; i++)
			for (int j = 0; j < N / 2; j++)
				v[i][j] = twobig(i * 2, j * 2);
		N /= 2;
	}
	cout << v[0][0];
}