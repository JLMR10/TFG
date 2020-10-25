import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from tfgApp.services import gameServices, userServices


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

        gameId = self.scope["url_route"]["kwargs"]["gameId"]
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
        ##prueba = json.loads(front_text)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            if loaded_dict_data.get("canvasArray") is not None \
                    or loaded_dict_data.get("chipsArray") is not None \
                    or loaded_dict_data.get("charactersArray") is not None:
                userId = self.scope["session"]["user"]["localId"]
                canvasArray = loaded_dict_data.get("canvasArray")
                chipsArray = loaded_dict_data.get("chipsArray")
                charactersArray = loaded_dict_data.get("charactersArray")
                myResponse = {
                    "canvasArray": canvasArray,
                    "chipsArray": chipsArray,
                    "charactersArray": charactersArray,
                    "sender": userId
                }

            elif loaded_dict_data.get("pythonUsersTurns"):
                myResponse = {
                    "pythonUsersTurns": loaded_dict_data.get("pythonUsersTurns"),
                    "userTurn": loaded_dict_data.get("userTurn"),
                    "endTurn": loaded_dict_data.get("endTurn"),
                }
            else:
                msg = loaded_dict_data.get("message")
                userId = self.scope["session"]["user"]["localId"]
                print(self.scope["session"]["user"])
                usersId = list(gameServices.getProperty(self.game_id, "Users").keys())
                users = userServices.getIdAndNamesFromUsersList(usersId)

                myResponse = {
                    "message": msg,
                    "username": users[userId],
                    "senderID": userId
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