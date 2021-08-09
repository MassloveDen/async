from time import time



def gen_file():
    while True:
        pattern = 'file-{}.jpeg'
        t = time()
        yield pattern.format(str(t))



def gen(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g = gen('Den')
g1 = gen2(4)

tasks = [g, g1]

while tasks:
    task = tasks.pop(0)

    try:
        i= next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

