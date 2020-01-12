#include <iostream>

using namespace std;

int main()
{
    int m;
    int n;
    int minGrayValue;
    int maxGrayValue;
    int targetGrayValue;
    int currentGrayValue;

    scanf("%d%d%d%d%d", &m, &n, &minGrayValue, &maxGrayValue, &targetGrayValue);

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &currentGrayValue);
            if (currentGrayValue >= minGrayValue && currentGrayValue <= maxGrayValue)
            {
                currentGrayValue = targetGrayValue;
            }

            if (j == n - 1)
            {
                printf("%03d\n", currentGrayValue);
            }
            else
            {
                printf("%03d ", currentGrayValue);
            }
        }
    }

    return 0;
}
