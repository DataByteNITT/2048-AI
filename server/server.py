#!/usr/bin/env python

import asyncio
import websockets
import getch

async def hello(websocket, path):
        
        while True:
            
            print("get inp")
            greeting = getch.getch()
            await websocket.send(str(greeting))
            print("> {}".format(greeting))
            
            resp = await websocket.recv()
            print(resp)

start_server = websockets.serve(hello, 'localhost', 9876)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

