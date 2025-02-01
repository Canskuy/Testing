import os
import asyncio
import time
from datetime import datetime
from KiritoRobot import DEV_USERS
from KiritoRobot import TEMP_DOWNLOAD_DIRECTORY as path
from KiritoRobot import telethn as tbot
from KiritoRobot.events import register

water = './KiritoRobot/resources/kirito.jpg'
client = tbot

@register(pattern=r"^/send ?(.*)")
async def Prof(event):
    if event.sender_id == DEV_USERS:
        pass
    else:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./KiritoRobot/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("No File Found!")


