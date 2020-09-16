import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from tfgApp.services import gameServices


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        gameId = self.scope["url_route"]["kwargs"]["gameId"]
        users = list(gameServices.getProperty(gameId, "Users").values())
        print(users)
        ##await asyncio.sleep(10)
        await self.send({
            "type": "websocket.send",
            "text": "Hello Arthur"
        })

    async def websocket_receive(self, event):
        print("received", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)