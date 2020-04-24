import asyncio
from urllib import parse
import json
room_online_member = set()

async def monitor_member(send):
    text = {
        "type": "websocket.send",
        "text": ""
    }
    last_set = {}
    #send current online member
    content = {
        "type": "monitor_member",
        "msg": list(room_online_member)
    }
    text["text"] = json.dumps(content)
    await send(text)
    while True:
        if not last_set:
            last_set = room_online_member.copy()
            continue
        else:
            if last_set == room_online_member:
                await asyncio.sleep(0.01)
                continue
            else:
                content = {
                    "type": "monitor_member",
                    "msg": list(room_online_member)
                }
                text["text"] = json.dumps(content)
                last_set = room_online_member.copy()
                await send(text)
                # add = room_online_member.difference(last_set)
                # remove = last_set.difference(room_online_member)
                # last_set = room_online_member.copy()
                # if add:
                #     print(f"{add}进入了房间", end=" ")
                # if remove:
                #     print(f"{remove}退出了房间", end=" ")
                # print(f"当前在房间人员:{room_online_member}")
        await asyncio.sleep(0.01)
