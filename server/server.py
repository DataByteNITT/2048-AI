#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket, path):
        
        while True:
            
            print("get inp")
            greeting = str(input())
            await websocket.send(str(greeting))
            print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 9876)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

