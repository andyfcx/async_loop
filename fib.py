import asyncio
from time import time


async def factorial(name, number):
    f = 1
    await asyncio.sleep(2)
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:
    t0 = time()
    L = await asyncio.gather(
        [factorial(str(i), i) for i in range(2,6)]
    )
    t1 = time()
    print(L)
    print(f"Elapsed time: {t1-t0}")


if __name__ == '__main__':
    asyncio.run(main())