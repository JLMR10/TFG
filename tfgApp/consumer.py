import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from tfgApp.services import gameServices


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

        gameId = self.scope["url_route"]["kwargs"]["gameId"]
        users = list(gameServices.getProperty(gameId, "Users").values())
        print(users)
        print(self.scope["session"]["user"]["email"])
        self.game_id = gameId
        print(self.game_id)

        await self.channel_layer.group_add(
            gameId,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })
        ##await asyncio.sleep(10)

    async def websocket_receive(self, event):
        print("received", event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get("message")
            userEmail = self.scope["session"]["user"]["email"]
            myResponse = {
                "message": msg,
                "username": userEmail
            }

            #broadcasts the message event to be sent
            await self.channel_layer.group_send(
                self.game_id,
                {
                    "type": "chat_message_event",
                    "text": json.dumps(myResponse)
                }
            )

    async def chat_message_event(self, event):
        # send the actual message
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })

    async def websocket_disconnect(self, event):
        print("disconnected", event)