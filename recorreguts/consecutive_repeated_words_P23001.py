import yogi

c = 0
j = 0
t = 1

fw = yogi.read(str)

for i in yogi.tokens(str):

    if j == 0 and i == fw:
        c = 1
    j = 1

    if i == fw:
        c += 1
        if c > t:
            t = c
    else:
        c = 0

print(t)