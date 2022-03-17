import os
import re
from platform import python_version as kontol
from telethon import events, Button
from TGN.events import register
from TGN import telethn as tbot


PHOTO = "https://telegra.ph/file/bd7b76ef72a68e15e954c.jpg"

@register(pattern=("/donate"))
async def awake(event):
  TEXT = f"**Donate for GodfatherBot 🔥❤️**"
  BUTTON = [[Button.url("Razorpay", "https://pages.razorpay.com/GODFATHERDONATIONS")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
