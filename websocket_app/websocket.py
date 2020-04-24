import datetime
import json
import asyncio
from websocket_app.monitor_room_member import monitor_member, room_online_member
from urllib import parse

msg = ""

async def websocket_application(scope, receive, send):
    global msg
    alias = parse.parse_qs(scope["query_string"].decode()).get('alias')[0]
    msg_task = asyncio.create_task(sendmsg(scope, send))
    monitor_task = asyncio.create_task(monitor_member(send))
    while True:
        
        event = await receive()

        if event['type'] == 'websocket.connect':
            room_online_member.add(alias)
            await send({
                'type': 'websocket.accept'
            })
            
        if event['type'] == 'websocket.disconnect':
            print(scope['client'], 'disconnected')
            msg_task.cancel()
            monitor_task.cancel()
            room_online_member.remove(alias)
            break
        if event['type'] == 'websocket.receive':
            ctx = json.loads(event['text'])
            ctx["time"] = str(datetime.datetime.now())
            ctx["type"] = "msg"
            msg = json.dumps(ctx)



              

async def sendmsg(scope, send):
    text = {
        "type": "websocket.send",
        "text": ""
    }
    last_msg = ""
    while True:
        if last_msg != msg:
            last_msg = text["text"] = msg
            await send(text)
        await asyncio.sleep(0.05)



