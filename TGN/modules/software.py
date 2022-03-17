# Magisk Module- Module from AstrakoBot
# Inspired from RaphaelGang's android.py
# By DAvinash97 & shado-hackers


from datetime import datetime
from bs4 import BeautifulSoup
from requests import get
from telegram import Bot, Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import CallbackContext, run_async
from ujson import loads
from yaml import load, Loader

from TGN import dispatcher
from TGN.modules.sql.clear_cmd_sql import get_clearcmd
from TGN.modules.github import getphh
from TGN.modules.helper_funcs.misc import delete



def checkfw(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    chat = update.effective_chat
    
    if len(args) == 2:
        temp, csc = args
        model = f'sm-' + temp if not temp.upper().startswith('SM-') else temp
        fota = get(
            f'http://fota-cloud-dn.ospserver.net/firmware/{csc.upper()}/{model.upper()}/version.xml'
        )

        if fota.status_code != 200:
            msg = f"Couldn't check for {temp.upper()} and {csc.upper()}, please refine your search or try again later!"

        else:
            page = BeautifulSoup(fota.content, 'lxml')
            os = page.find("latest").get("o")

            if page.find("latest").text.strip():
                msg = f'*Latest released firmware for {model.upper()} and {csc.upper()} is:*\n'
                pda, csc, phone = page.find("latest").text.strip().split('/')
                msg += f'• PDA: `{pda}`\n• CSC: `{csc}`\n'
                if phone:
                    msg += f'• Phone: `{phone}`\n'
                if os:
                    msg += f'• Android: `{os}`\n'
                msg += ''
            else:
                msg = f'*No public release found for {model.upper()} and {csc.upper()}.*\n\n'

    else:
        msg = 'Give me something to fetch, like:\n`/checkfw SM-N975F DBT`'

    delmsg = message.reply_text(
        text = msg,
        parse_mode = ParseMode.MARKDOWN,
        disable_web_page_preview = True,
    )

    cleartime = get_clearcmd(chat.id, "checkfw")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)


def getfw(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    chat = update.effective_chat
    btn = ""
    
    if len(args) == 2:
        temp, csc = args
        model = f'sm-' + temp if not temp.upper().startswith('SM-') else temp
        fota = get(
            f'http://fota-cloud-dn.ospserver.net/firmware/{csc.upper()}/{model.upper()}/version.xml'
        )

        if fota.status_code != 200:
            msg = f"Couldn't check for {temp.upper()} and {csc.upper()}, please refine your search or try again later!"

        else:
            url1 = f'https://samfrew.com/model/{model.upper()}/region/{csc.upper()}/'
            url2 = f'https://www.sammobile.com/samsung/firmware/{model.upper()}/{csc.upper()}/'
            url3 = f'https://sfirmware.com/samsung-{model.lower()}/#tab=firmwares'
            url4 = f'https://samfw.com/firmware/{model.upper()}/{csc.upper()}/'
            fota = get(
                f'http://fota-cloud-dn.ospserver.net/firmware/{csc.upper()}/{model.upper()}/version.xml'
            )
            page = BeautifulSoup(fota.content, 'lxml')
            os = page.find("latest").get("o")
            msg = ""
            if page.find("latest").text.strip():
                pda, csc2, phone = page.find("latest").text.strip().split('/')
                msg += f'*Latest firmware for {model.upper()} and {csc.upper()} is:*\n'
                msg += f'• PDA: `{pda}`\n• CSC: `{csc2}`\n'
                if phone:
                    msg += f'• Phone: `{phone}`\n'
                if os:
                    msg += f'• Android: `{os}`\n'
            msg += '\n'
            msg += f'*Downloads for {model.upper()} and {csc.upper()}*\n'
            btn = [[InlineKeyboardButton(text=f"samfrew.com", url = url1)]]
            btn += [[InlineKeyboardButton(text=f"sammobile.com", url = url2)]]
            btn += [[InlineKeyboardButton(text=f"sfirmware.com", url = url3)]]
            btn += [[InlineKeyboardButton(text=f"samfw.com", url = url4)]]
    else:
        msg = 'Give me something to fetch, like:\n`/getfw SM-N975F DBT`'

    delmsg = message.reply_text(
        text = msg,
        reply_markup = InlineKeyboardMarkup(btn),
        parse_mode = ParseMode.MARKDOWN,
        disable_web_page_preview = True,
    )

    cleartime = get_clearcmd(chat.id, "getfw")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)




def miui(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    device = message.text[len("/miui ") :]
    markup = []

    if device:
        link = "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/miui-updates-tracker/master/data/latest.yml"
        yaml_data = load(get(link).content, Loader=Loader)
        data = [i for i in yaml_data if device in i['codename']]

        if not data:
            msg = f"Miui is not avaliable for {device}"
        else:
            for fw in data:
                av = fw['android']
                branch = fw['branch']
                method = fw['method']
                link = fw['link']
                fname = fw['name']
                version = fw['version']
                size = fw['size']
                btn = fname + ' | ' + branch + ' | ' + method + ' | ' + version + ' | ' + av + ' | ' + size
                markup.append([InlineKeyboardButton(text = btn, url = link)])

            device = fname.split(" ")
            device.pop()
            device = " ".join(device)
            msg = f"The latest firmwares for the *{device}* are:"
    else:
        msg = 'Give me something to fetch, like:\n`/miui whyred`'

    delmsg = message.reply_text(
        text = msg,
        reply_markup = InlineKeyboardMarkup(markup),
        parse_mode = ParseMode.MARKDOWN,
        disable_web_page_preview = True,
    )

    cleartime = get_clearcmd(chat.id, "miui")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)
#Don't kang it. Create by shado_hackers in telegram 

def realmeui(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    device = message.text[len("/realmeui ") :]
    markup = []

    if device:
        link = "https://raw.githubusercontent.com/RealmeUpdater/realme-updates-tracker/master/data/latest.yml"
        yaml_data = load(get(link).content, Loader=Loader)
        data = [i for i in yaml_data if device in i['codename']]

        if not data:
            msg = f"realme ui is not avaliable for {device}"
        else:
            for fw in data:
                av = fw['android']
                branch = fw['branch']
                method = fw['method']
                link = fw['link']
                fname = fw['name']
                version = fw['version']
                size = fw['size']
                btn = fname + ' | ' + branch + ' | ' + method + ' | ' + version + ' | ' + av + ' | ' + size
                markup.append([InlineKeyboardButton(text = btn, url = link)])

            device = fname.split(" ")
            device.pop()
            device = " ".join(device)
            msg = f"The latest firmwares for the *{device}* are:"
    else:
        msg = 'Give me something to fetch, like:\n`/realmeui RMX2061`'

    delmsg = message.reply_text(
        text = msg,
        reply_markup = InlineKeyboardMarkup(markup),
        parse_mode = ParseMode.MARKDOWN,
        disable_web_page_preview = True,
    )

    cleartime = get_clearcmd(chat.id, "realmeui")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)






GETFW_HANDLER = CommandHandler("getfw", getfw, run_async=True)
CHECKFW_HANDLER = CommandHandler("checkfw", checkfw, run_async=True)
MIUI_HANDLER = CommandHandler("miui", miui, run_async=True)
REALMEUI_HANDLER  = CommandHandler("realmeui", realmeui, run_async=True)




dispatcher.add_handler(GETFW_HANDLER)
dispatcher.add_handler(CHECKFW_HANDLER)
dispatcher.add_handler(REALMEUI_HANDLER)
dispatcher.add_handler(MIUI_HANDLER)

__mod_name__ = "software"
__command_list__ = [ "checkfw", "getfw", "miui", "realmeui"]
__handlers__ = [GETFW_HANDLER, CHECKFW_HANDLER,  MIUI_HANDLER, REALMEUI_HANDLER]
