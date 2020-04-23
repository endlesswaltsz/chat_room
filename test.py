import asyncio

l = [{'a':1, 'time':10, 'g':60},{'a':2, 'time':12, 'g':50}]


async def get_update():
    while True:
        res = list(filter(lambda x: x['time'] > 10 and x['g'] > 50, l))
        if not res:
            await asyncio.sleep(0.5)
            print(res)
            continue
        else:
            return res
async def append():
    await asyncio.sleep(3)
    l.append({'a':2, 'time':12, 'g':60})

async def main():
    return await asyncio.gather(
        get_update(),
        append(),
    )


res = asyncio.run(main())
print(res[0])