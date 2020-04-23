import asyncio
room_online_member = {"夏斌"}

async def monitor_member():
    last_set = {}
    print(f"当前在房间人员:{room_online_member}")
    while True:
        if not last_set:
            last_set = room_online_member.copy()
            continue
        else:
            if last_set == room_online_member:
                await asyncio.sleep(0.01)
                continue
            else:
                add = room_online_member.difference(last_set)
                remove = last_set.difference(room_online_member)
                last_set = room_online_member.copy()
                if add:
                    print(f"{add}进入了房间", end=" ")
                if remove:
                    print(f"{remove}退出了房间", end=" ")
                print(f"当前在房间人员:{room_online_member}")
        await asyncio.sleep(0.01)

async def main():
    task = asyncio.create_task(monitor_member())
    await asyncio.sleep(2)
    room_online_member.add("黄子轩")
    await asyncio.sleep(0.2)
    room_online_member.add("黄泽霖")
    await asyncio.sleep(2)
    room_online_member.add("冲哥")
    await asyncio.sleep(2)
    room_online_member.remove("冲哥")
    await asyncio.sleep(2)

asyncio.run(main())