#!/usr/bin/env python

import asyncio
import websockets
import json
#import getch

async def consumer(message):
    print ("GOT YOUR MESSAGE")

async def hello(websocket, path):

    while True:

        print("get inp")
        # greeting =send()
        # await websocket.send(str(greeting))
        # print("> {}".format(greeting))

        message = await websocket.recv()
        await consumer(message)
        # data = json.loads(resp)
        print("Recieved Game State : {}".format(data))
start_server = websockets.serve(hello, 'localhost', 9876)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

def send(data):
    pass


def receive():
    pass
