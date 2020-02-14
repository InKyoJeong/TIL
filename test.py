import sys

input = sys.stdin.readline
arr = []
for i in range(int(input())):

    sign = input().rstrip().split(' ')

    if sign[0] == 'push':
        arr.append(sign[1])
    elif sign[0] == 'pop':
        if len(arr) == 0:
            print('-1')
        else:
            print(arr.pop())
    elif sign[0] == 'size':
        print(len(arr))
    elif sign[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif sign[0] == 'top':
        if len(arr) == 0:
            print('-1')
        else:
            print(arr[len(arr)-1])
