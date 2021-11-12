import random

com = set()
while len(com) < 6:
    x = random.randint(1,48)
    com.add(x)
print('開出的號碼:',com)

times = 0
while True:
    me = set()
    while len(me) < 6:
        n = random.randint(1,48)
        me.add(n)
    print('我買的號碼:',me)
    times += 1

    total = 0
    for i in com:
        if i in me:
            total += 1
    print('中了',total,'個號碼')
    if total >= 4:
        break
print('我總共買了:',times,'張')