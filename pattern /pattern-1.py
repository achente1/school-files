
for i in range(5):
    for c in range(i+1):
        print('*',end='')
    print()


for i in range(6):
    for c in range(i):
        print(1,end='')
    print()

for i in range(1,5):
    for c in range(i):
        print(i,end='')
    print()


for i in range(1,6):
    for r in range(i):
        print(r+1,end='')
    print()

for i in range(6,1,-1):
    for r in range(1,i):
        print(r,end='')
    print()


n=65
for i in range(1,5):
    for r in range(i):
        print(chr(n),end='')
        n+=1
    print()


n=65
for i in range(1,5):
    for r in range(i):
        print(chr(n),end='')
    print()
    n+=1

for i in range(1,5):
    n=65
    for r in range(i):
        print(chr(n),end='')
        n+=1
    print()


for i in range(4,0,-1):
    for r in range(i,0,-1):
        print(r,end='')
    print()