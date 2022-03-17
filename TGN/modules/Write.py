import functools

import requests
from pyrogram import filters

from TGN.function.pluginhelpers import get_text
from TGN import pbot

API1 = "https://single-developers.up.railway.app?write="
API2 = "https://single-developers.up.railway.app/write"


def is_admin(func):
    @functools.wraps(func)
    async def oops(client, message):
        is_admin = False
        try:
            user = await message.chat.get_member(message.from_user.id)
            admin_strings = ("creator", "administrator")
            if user.status not in admin_strings:
                is_admin = False
            else:
                is_admin = True

        except ValueError:
            is_admin = True
        if is_admin:
            await func(client, message)
        else:
            await message.reply("**Only Admins can execute this command!**")

    return oops


@pbot.on_message(filters.command("write") & ~filters.edited & ~filters.bot)
async def writer(client, message):
    if message.reply_to_message:
        try:
            msg = await client.send_message(message.chat.id, "**Writing the text....**")
        except:
            return
        try:
            text = get_text(message.reply_to_message)
        except:
            return
        if (
            message.reply_to_message.video
            or message.reply_to_message.document
            or message.reply_to_message.photo
            or message.reply_to_message.animation
            or message.reply_to_message.sticker
        ):
            try:
                await msg.edit("Sorry I can't get the text of replied message")
                return
            except:
                return
        if not text:
            try:
                await msg.edit("**Invalid Command Syntax**\n\n`/write [name]`")
                return
            except:
                return
        try:
            req = requests.get(API1 + text.replace(" ", "%20"))
        except:
            return
        try:
            url = req.history[1].url
        except:
            return
        try:
            await msg.delete()
        except:
            return
        try:
            await message.reply_photo(
                url,
                caption=f"**Successfully Written** As {text}\n\nImage Link => {url}\n\n**By @kigo_omfo**",
            )
        except:
            return

    else:
        try:
            msg = await client.send_message(message.chat.id, "**Writing the text....**")
        except:
            return
        try:
            text = get_text(message)
        except:
            return
        if not text:
            try:
                await msg.edit("**Invalid Command Syntax**\n\n`/write [name]`")
                return
            except:
                return
        try:
            req = requests.get(API1 + text.replace(" ", "%20"))
        except:
            return
        try:
            url = req.history[1].url
        except:
            return
        try:
            await msg.delete()
        except:
            return
        try:
            await message.reply_photo(
                url,
                caption=f"**Successfully Written** As {text}\n\nImage Link => {url}\n\n**By @kigo_omfo**",
            )
        except:
            return


@pbot.on_message(filters.command("longwrite") & ~filters.edited & ~filters.bot)
async def longwriter(client, message):
    if message.reply_to_message:
        try:
            msg = await client.send_message(message.chat.id, "**Writing the text....**")
        except:
            return
        try:
            text = get_text(message.reply_to_message)
        except:
            return
        if (
            message.reply_to_message.video
            or message.reply_to_message.document
            or message.reply_to_message.photo
            or message.reply_to_message.animation
            or message.reply_to_message.sticker
        ):
            try:
                await msg.edit("Sorry I can't get the text of replied message")
                return
            except:
                return
        if not text:
            try:
                await msg.edit("**Invalid Command Syntax**\n\n`/write [name]`")
                return
            except:
                return
        try:
            body = {"text": f"{text}"}
        except:
            return
        try:
            req = requests.get(
                API2, headers={"Content-Type": "application/json"}, json=body
            )
        except:
            return
        try:
            url = req.history[1].url
        except:
            return
        try:
            await msg.delete()
        except:
            return
        try:
            await message.reply_photo(
                url,
                caption=f"**Successfully Written**\n\nImage Link => {url}\n\n**By @TGN_Ro_bot**",
            )
        except:
            return

    else:
        try:
            msg = await client.send_message(message.chat.id, "**Writing the text....**")
        except:
            return
        try:
            text = get_text(message)
        except:
            return
        if not text:
            try:
                await msg.edit("**Invalid Command Syntax**\n\n`/write [name]`")
                return
            except:
                return
        try:
            body = {"text": f"{text}"}
        except:
            return
        try:
            req = requests.get(
                API2, headers={"Content-Type": "application/json"}, json=body
            )
        except:
            return
        try:
            url = req.history[1].url
        except:
            return
        try:
            await msg.delete()
        except:
            return
        try:
            await message.reply_photo(
                url,
                caption=f"**Successfully Written**\n\nImage Link => {url}\n\n**By @TGN_Ro_bot**",
            )
        except:
            return
