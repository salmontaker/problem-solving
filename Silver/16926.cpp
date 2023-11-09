#include <iostream>
using namespace std;

int N, M, R;
int A[301][301];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> R;
    for (int y = 0; y < N; y++)
        for (int x = 0; x < M; x++)
            cin >> A[y][x];

    for (int r = 0; r < R; r++)
    {
        for (int d = 0; d < min(N, M) / 2; d++)
        {
            int y_max = N - d - 1;
            int x_max = M - d - 1;
            int temp = A[d][d];

            for (int x = d; x < x_max; x++)
                A[d][x] = A[d][x + 1];
            for (int y = d; y < y_max; y++)
                A[y][x_max] = A[y + 1][x_max];
            for (int x = x_max; x > d; x--)
                A[y_max][x] = A[y_max][x - 1];
            for (int y = y_max; y > d; y--)
                A[y][d] = A[y - 1][d];

            A[d + 1][d] = temp;
        }
    }

    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < M; x++)
            cout << A[y][x] << ' ';
        cout << '\n';
    }
}