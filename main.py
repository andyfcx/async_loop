import asyncio
from time import time


async def call_model(n):
    await asyncio.sleep(3)
    print(f"[task] {n}")


async def main():
    await asyncio.gather(*[call_model(i) for i in range(5)])


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    t1 = time()
    print(f"Elapsed time: {t1-t0}")