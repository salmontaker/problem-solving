#include <bits/stdc++.h>
using namespace std;

int N, K, B[201][201];
int S, Y, X;
deque<tuple<int, int, int>> V, T;
int dy[4] = {1, 0, -1, 0};
int dx[4] = {0, 1, 0, -1};

int main()
{
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> K;
    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < N; x++)
        {
            cin >> B[y][x];
            if (B[y][x] != 0)
                V.push_back({B[y][x], y, x});
        }
    }

    cin >> S >> Y >> X;
    sort(V.begin(), V.end());

    while (S--)
    {
        while (!V.empty())
        {
            auto [n, y, x] = V.front();
            V.pop_front();

            for (int i = 0; i < 4; i++)
            {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (-1 < ny && ny < N && -1 < nx && nx < N && B[ny][nx] == 0)
                {
                    B[ny][nx] = n;
                    T.push_back({B[ny][nx], ny, nx});
                }
            }
        }
        V = T;
        T.clear();
    }

    cout << B[Y - 1][X - 1];
}