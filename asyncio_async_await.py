import asyncio
from time import time



async def print_n():
    n = 1
    while True:
        print(n)
        n += 1
        await asyncio.sleep(0.5)



async def print_t():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} sec have pass".format(count))
        count += 1
        await asyncio.sleep(1)



async def main():
    task1 = asyncio.create_task(print_n())
    task2 = asyncio.create_task(print_t())

    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())


