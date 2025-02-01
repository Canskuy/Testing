import os
import re

from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from KiritoRobot.events import register
from KiritoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/9c451f04faacc45b89e53.jpg"

@register(pattern=("/alive"))
async def awake(event):
  ken = event.sender.first_name
  TEXT = f"**Hi {ken}, I'm Kirito Robot.** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += f"⚪ **My Master : [can](https://t.me/thatscan)** \n\n"
  TEXT += f"⚪ **Library Version :** `{telever}`\n\n"
  TEXT += f"⚪ **Python Version :** `3.9.7` \n\n"
  TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/KiritoxRobot?start=help"), Button.url("Support", "https://t.me/kiritosupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
