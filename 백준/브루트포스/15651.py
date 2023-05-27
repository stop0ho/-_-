import sys
n, m = map(int, input().split())

ans = [0] * m

# index번째의 수열 결정하는 함수
def P(n, m, index):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(1, n+1):
        ans[index] = i
        P(n, m, index+1)

P(n, m, 0)

