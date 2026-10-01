# wap to find the following patterns
'''

1
13
135
1357

4321
432
43
4

'''

for i in range(4):
    for j in range(4,i,-1):
        print(j,end='')
    print()

for i in range(1,5):
    for j in range(1,i*2,2):
        print(j,end='')
    print()
