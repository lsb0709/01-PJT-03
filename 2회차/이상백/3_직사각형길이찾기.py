import sys

sys.stdin = open("_직사각형길이찾기.txt")
T = int(input())

for test in range(1, T+1):
    a, b, c = map(int, input().split())

    result = ''

    if a == b :
        result = c
    elif a == c :
        result = b
    else :
        result = a
    print(f'#{test} {result}')