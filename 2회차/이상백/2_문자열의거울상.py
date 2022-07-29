import sys

sys.stdin = open("_문자열의거울상.txt")
T = int(input())
for test in range(1, T + 1):
        
        str_ = input()
        str = str_[::-1]
        
        result = ''
        for i in range(len(str)):
            if str[i] == 'q':
                result += 'p'
            elif str[i] == 'p':
                result += 'q'
            elif str[i] == 'd':
                result += 'b'
            else:
                result += 'd'
        print(f'#{test} {result}')