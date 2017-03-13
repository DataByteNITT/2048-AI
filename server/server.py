#!/usr/bin/env python

import asyncio
import websockets
import json
#import getch

async def hello(websocket, path):
		
		while True:
			
			print("get inp")
			greeting = input()
			await websocket.send(str(greeting))
			print("> {}".format(greeting))
			
			resp = await websocket.recv()
			data = json.loads(resp)            
			print("Recieved Game State : {}".format(data))
start_server = websockets.serve(hello, 'localhost', 9876)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

