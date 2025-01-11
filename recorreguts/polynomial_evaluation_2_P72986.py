import yogi

eval = 0

x = yogi.read(float)

for i in yogi.tokens(float):
    eval = (eval*x + i)

print('{:.4f}'.format(eval))