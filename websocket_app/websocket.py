import datetime
import json
import asyncio
import json

msg = ""

async def websocket_application(scope, receive, send):
    task = asyncio.create_task(sendmsg(send))
    while True:
        event = await receive()

        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })
            print(scope['client'], 'connected')

        if event['type'] == 'websocket.disconnect':
            print(scope['client'], 'disconnected')
            task.cancel()
            break
        if event['type'] == 'websocket.receive':
            ctx = json.loads(event['text'])
            ctx["time"] = datetime.datetime.now()
            msg.append(ctx)
            msg = json.dumps(ctx)



              

async def sendmsg(send):
    text = {
        "type": "websocket.send",
        "text": ""
    }
    last_msg = ""
    while True:
        if not last_msg:
            last_msg = msg
            continue
        if last_msg == msg:
            continue
        last_msg = text["text"] = msg
        send(text)
        await asyncio.sleep(0.05)



