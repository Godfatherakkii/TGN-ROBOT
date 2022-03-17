# Copyright (c) 2021 Itz-fork
# Part of: Nexa-Userbot
# re-write for Rose by szsupunma


import os
from pyrogram import filters
from pyrogram.types import Message
from re import search
from TGN import pbot as NEXAUB
from TGN.utils.permissions import adminsOnly
from TGN import pbot as app
from TGN.utils.dbfunctions import set_anti_func , get_anti_func, del_anti_func
from re import compile
from tokenize import group
from TGN.utils.filter_groups import antifunc_group
from TGN.services.keyboard import ikb
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,  Message

#help for anyother modules
async def edit_or_reply(message, text, parse_mode="md"):
    if message.from_user.id:
        if message.reply_to_message:
            kk = message.reply_to_message.message_id
            return await message.reply_text(
                text, reply_to_message_id=kk, parse_mode=parse_mode
            )
        return await message.reply_text(text, parse_mode=parse_mode)
    return await message.edit(text, parse_mode=parse_mode)

#lag tool
class REGEXES:
    """
    Regexes Class
    Included Regexes:
        arab: Arabic Language
        chinese: Chinese Language
        japanese: Japanese Language (Includes Hiragana, Kanji and Katakana)
        sinhala: Sinhala Language
        tamil: Tamil Language
        cyrillic: Cyrillic Language
    """

    arab = compile('[\u0627-\u064a]')
    chinese = compile('[\u4e00-\u9fff]')
    japanese = compile('[(\u30A0-\u30FF|\u3040-\u309Fー|\u4E00-\u9FFF)]')
    sinhala = compile('[\u0D80-\u0DFF]')
    tamil = compile('[\u0B02-\u0DFF]')
    cyrillic = compile('[\u0400-\u04FF]')


#arg
def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

# Enable anti-arab
@app.on_message(
    filters.command("antiarabic") & ~filters.edited & ~filters.bot & ~filters.private
)
@adminsOnly("can_delete_messages")
async def on_off_antiarab(_, message: Message):
    sex = await edit_or_reply(message, "`Processing...`")
    args = get_arg(message)
    if not args:
        return await sex.edit(f"""
Usage: /antiarabic `[on | off]`
""")
    lower_args = args.lower()
    if lower_args == "on":
        await set_anti_func(message.chat.id, "on", "ar")
    elif lower_args == "off":
        await del_anti_func(message.chat.id)
    else:
        return await sex.edit(f"""
Usage: /antiarabic `[on | off]`
""")
    await sex.edit(f"✅ **Successfully** `{'Enabled' if lower_args=='on' else 'Disabled'}` **Arabic Detection Guard**")

# Enable anti-chinesee
@app.on_message(
    filters.command("antichinese") & ~filters.edited & ~filters.bot & ~filters.private
)
@adminsOnly("can_delete_messages")
async def on_off_antiarab(_, message: Message):
    lel = await edit_or_reply(message, "`Processing...`")
    args = get_arg(message)
    if not args:
        return await lel.edit(f"""
Usage: /antichinese `[on | off]`
""")
    lower_args = args.lower()
    if lower_args == "on":
        await set_anti_func(message.chat.id, "on", "ac")
    elif lower_args == "off":
        await del_anti_func(message.chat.id)
    else:
        return await lel.edit(f"""
Usage: /antichinese `[on | off]`
""")
    await lel.edit(f"✅ **Successfully** `{'Enabled' if lower_args=='on' else 'Disabled'}` **Chinese Detection Guard**")

# Enable anti-japanese
@app.on_message(
    filters.command("antijapanese") & ~filters.edited & ~filters.bot & ~filters.private
)
@adminsOnly("can_delete_messages")
async def on_off_antiarab(_, message: Message):
    sum = await edit_or_reply(message, "`Processing...`")
    args = get_arg(message)
    if not args:
        return await sum.edit(f"""
Usage: /antijapanese`[on | off]`
""")
    lower_args = args.lower()
    if lower_args == "on":
        await set_anti_func(message.chat.id, "on", "aj")
    elif lower_args == "off":
        await del_anti_func(message.chat.id)
    else:
        return await sum.edit(f"""
Usage: /antijapanese `[on | off]`
""")
    await sum.edit(f"✅ **Successfully** `{'Enabled' if lower_args=='on' else 'Disabled'}` **Japanese Detection Guard**")

# Enable anti-russian
@app.on_message(
    filters.command("antirussian") & ~filters.edited & ~filters.bot & ~filters.private
)
@adminsOnly("can_delete_messages")
async def on_off_antiarab(_, message: Message):
    sax = await edit_or_reply(message, "`Processing...`")
    args = get_arg(message)
    if not args:
        return await sax.edit(f"""
Usage: /antirussian `[on | off]`
""")
    lower_args = args.lower()
    if lower_args == "on":
        await set_anti_func(message.chat.id, "on", "au")
    elif lower_args == "off":
        await del_anti_func(message.chat.id)
    else:
        return await sax.edit(f"""
Usage: /antirussian `[on | off]`
""")
    await sax.edit(f"✅ **Successfully** `{'Enabled' if lower_args=='on' else 'Disabled'}` **Russian Detection Guard**")

# Enable anti-Sinhala ~ szsupunma
@app.on_message(
    filters.command("antisinhala") & ~filters.edited & ~filters.bot & ~filters.private
)
@adminsOnly("can_delete_messages")
async def on_off_antiarab(_, message: Message):
    sax = await edit_or_reply(message, "`Processing...`")
    args = get_arg(message)
    if not args:
        return await sax.edit(f"""
Usage: /sinhala `[on | off]`
""")
    lower_args = args.lower()
    if lower_args == "on":
        await set_anti_func(message.chat.id, "on", "si")
    elif lower_args == "off":
        await del_anti_func(message.chat.id)
    else:
        return await sax.edit(f"""
Usage: /antisinhala `[on | off]`
""")
    await sax.edit(f"✅ **Successfully** `{'Enabled' if lower_args=='on' else 'Disabled'}` **Sinhala Detection Guard**")

# Enable anti-Tamil
@app.on_message(
    filters.command("antitamil") & ~filters.edited & ~filters.bot & ~filters.private
)
@adminsOnly("can_delete_messages")
async def on_off_antiarab(_, message: Message):
    sax = await edit_or_reply(message, "`Processing...`")
    args = get_arg(message)
    if not args:
        return await sax.edit(f"""
Usage: /antitamil `[on | off]`
""")
    lower_args = args.lower()
    if lower_args == "on":
        await set_anti_func(message.chat.id, "on", "au")
    elif lower_args == "off":
        await del_anti_func(message.chat.id)
    else:
        return await sax.edit(f"""
Usage: /antitamil `[on | off]`
""")
    await sax.edit(f"✅ **Successfully** `{'Enabled' if lower_args=='on' else 'Disabled'}` **Tamil Detection Guard**")

#show antilang stas 
@app.on_message(
    filters.command("antilang") & ~filters.edited & ~filters.bot & ~filters.private
)
@adminsOnly("can_delete_messages")
async def on_off_antiarab(_, message: Message):
    sax = await edit_or_reply(message, "`Processing...`")
    await sax.edit(f"""
    
 • /antiarabic `[on | off]` :  **anti-arab function** 🚷
 • /antichinese `[on | off]` :  **anti-chinese function** 🇨🇳
 • /antijapanese `[on | off]` :  **anti-japanese function** 🇯🇵
 • /antirussian `[on | off]` :  **anti-russian function** 🇷🇺
 • /antisinhala `[on | off]` :  **anti-sinhala function** 🇱🇰
 • /antitamil `[on | off]` :  **anti-tamilfunction** 🇮🇳
    
    """)



# Listen to new members and checks
ANTIF_WARNS_DB = {}
ANTIF_TO_DEL = {}

WARN_EVEN_TXT = """
**Warn Event❕**
**User:** {}
**Anti-Language - detected** : ` {} `
**Be careful ⚠️**: `You have {}/3 warns, after that you'll be banned forever!`
"""

BAN_EVENT_TXT = """
**Ban Event❗**
**User:** {}
**Anti-Language - detected** : ` {} `
"""

FORM_AND_REGEXES = {
    "ar": [REGEXES.arab, "arabic"],
    "zh": [REGEXES.chinese, "chinese"],
    "jp": [REGEXES.japanese, "japanese"],
    "rs": [REGEXES.cyrillic, "russian"],
    "si": [REGEXES.sinhala, "sinhala"],
    "ta": [REGEXES.tamil, "Tamil"]
}

async def anti_func_handler(_, __, msg):
    chats = await get_anti_func(msg.chat.id)
    if chats:
        return True
    else:
        False

# Function to check if the user is an admin
async def check_admin(msg, user_id):
    if msg.chat.type in ["group", "supergroup", "channel"]:
        how_usr = await msg.chat.get_member(user_id)
        if how_usr.status in ["creator", "administrator"]:
            return True
        else:
            return False
    else:
        return True

async def check_afdb(user_id):
    if user_id in ANTIF_WARNS_DB:
        ANTIF_WARNS_DB[user_id] += 1
        if ANTIF_WARNS_DB[user_id] >= 3:
            return True
        return False
    else:
        ANTIF_WARNS_DB[user_id] = 1
        return False

async def check_admin(msg, user_id):
    if msg.chat.type in ["group", "supergroup", "channel"]:
        how_usr = await msg.chat.get_member(user_id)
        if how_usr.status in ["creator", "administrator"]:
            return True
        else:
            return False
    else:
        return True

# Function to warn or ban users
async def warn_or_ban(message, mode):
    # Users list
    users = message.new_chat_members
    chat_id = message.chat.id
    # Obtaining user who sent the message
    tuser = message.from_user
    try:
        mdnrgx = FORM_AND_REGEXES[mode]
        if users:
            for user in users:
                if any(search(mdnrgx[0], name) for name in [user.first_name, user.last_name]):
                    await NEXAUB.ban_chat_member(chat_id, user.id)
                    await message.reply(BAN_EVENT_TXT.format(user.mention, mdnrgx[1]),reply_markup=InlineKeyboardMarkup(
                    [
                        InlineKeyboardButton(
                            "❕ Unban", callback_data=f"unban_{chat_id}_{tuser}"
                        )
                    ]),
                    
                    
                    )
        elif message.text:
            if not tuser:
                return
            if search(mdnrgx[0], message.text):
                await message.delete()
                # Admins have the foking power
                if not await check_admin(message, tuser.id):
                    # Ban the user if the warns are exceeded
                    if await check_afdb(tuser.id):
                        await NEXAUB.ban_chat_member(chat_id, tuser.id)
                        await message.reply(BAN_EVENT_TXT.format(tuser.mention, mdnrgx[1]))
                    keyboard = ikb({"🚨  Remove Warn  🚨": f"unwarn_{tuser.id}"})
                    rp = await message.reply(WARN_EVEN_TXT.format(tuser.mention, mdnrgx[1], ANTIF_WARNS_DB[tuser.id]),reply_markup=keyboard)
                    if chat_id in ANTIF_TO_DEL:
                        await NEXAUB.delete_messages(chat_id=chat_id, message_ids=ANTIF_TO_DEL[chat_id])
                    ANTIF_TO_DEL[chat_id] = [rp.message_id]
    except:
        pass

@app.on_callback_query(filters.regex("^unban_."))
async def cb_handler(bot, query):
    cb_data = query.data
    an_id = cb_data.split("_")[-1]
    chat_id = cb_data.split("_")[-2]
    user = await bot.get_chat_member(chat_id, query.from_user.id)
    if user.status not in ["creator", "administrator"]:
         return await query.answer("You can't do this need admin power 😶", show_alert=True)
    await bot.resolve_peer(an_id)
    res = await query.message.chat.unban_member(an_id)
    chat_data = await bot.get_chat(an_id)
    mention = f"@{chat_data.username}" if chat_data.username else chat_data.title
    if res:
        await query.message.reply_text(
                f"{mention} **has been unbanned by** {query.from_user.mention}"
            )
        await query.message.edit_reply_markup(reply_markup=None)


anti_chats = filters.create(func=anti_func_handler)

# I know there is lots of code duplication but oh well, IDGF
@app.on_message(
    (     filters.document
        | filters.photo
        | filters.sticker
        | filters.animation
        | filters.video
        | filters.text
        | ~filters.private 
        | ~filters.channel 
        | ~filters.bot),
        group = antifunc_group)
async def check_anti_funcs(_, message: Message):
    if message.sender_chat:
        return
    anti_func_det = await get_anti_func(message.chat.id)
    # Checks if the functions are enabled for the chat
    if not anti_func_det:
        return
    if anti_func_det[0] != "on":
        return
    # Warns or ban the user from the chat
    await warn_or_ban(message, anti_func_det[1])

__mod_name__ = "Anti-lang"
__help__ = """
Delete messages containing characters from one of the following automatically
- Arabic Language
- Chinese Language
- Japanese Language (Includes Hiragana, Kanji and Katakana)
- Sinhala Language
- Tamil Language
- Cyrillic Language

**Admin Commands:**
- /antilang - viwe pannel
- /antiarabic `[on | off]` -  anti-arab function
- /antichinese `[on | off]` -  anti-chinese function
- /antijapanese `[on | off]` -  anti-japanese function
- /antirussian `[on | off]` -  anti-russian function
- /antisinhala `[on | off]` -  anti-sinhala function
- /antitamil `[on | off]` -  anti-tamilfunction

**Note** : If admin send any containing characters in this lang when on  any function
           it will delete and user send 3 warn and after ban him       
 """
