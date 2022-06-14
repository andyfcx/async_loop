import asyncio


class TypeOne():
    def __init__(self, param):
        loop = asyncio.get_event_loop()
        self.member = loop.run_until_complete(create_member(param))


class TypeTwo():
    async def __ainit__(self, param):
        self.member = await create_member(param)
        print("OK")

    def __init__(self, param):
        asyncio.run(self.__ainit__(param))
        print("ASYNC DONE")


async def create_member(x):
    await asyncio.sleep(1)
    return x**2


def main():
    t1 = TypeOne(10)
    t2 = TypeTwo(10)
    print(t1.member)
    print(t2.member)


if __name__ == "__main__":
    main()
