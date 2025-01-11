import yogi

n = yogi.read(int)

for i in range(1, 11):
    p = n*i
    print(f'{n}*{i} = {p}')