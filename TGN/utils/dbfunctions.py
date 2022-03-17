import codecs
import pickle
from typing import Dict, List, Union

from TGN.mongo import db

restart_stagedb = db.restart_stage
captchadb = db.captcha
solved_captcha_db = db.solved_captcha
captcha_cachedb = db.captcha_cache
flood_toggle_db = db.flood_toggle
warnsdb = db.warns
antiservicedb = db.antiservice
nexaub_antif = db.nexa_mongodb
filtersdb = db.filters
usersdb = db.users
groupsdb = db.groups
nightdb = db.night
lockurl = db.locksu
captchadb = db.botlock
chatsdb = db.chats
usersdb = db.users

async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def get_served_chats() -> list:
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"chat_id": chat_id})


async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users = usersdb.find({"user_id": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in await users.to_list(length=1000000000):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})
async def is_b_on(chat_id: int) -> bool:
    chat = await captchadb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def b_off(chat_id: int):
    is_captcha = await is_b_on(chat_id)
    if not is_captcha:
        return
    return await captchadb.delete_one({"chat_id": chat_id})


async def b_on(chat_id: int):
    is_captcha = await is_b_on(chat_id)
    if is_captcha:
        return
    return await captchadb.insert_one({"chat_id": chat_id})

def add_chat(chat_id):
    stark = lockurl.find_one({"chat_id": chat_id})
    if stark:
        return False
    else:
        lockurl.insert_one({"chat_id": chat_id})
        return True


def remove_chat(chat_id):
    stark = lockurl.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        lockurl.delete_one({"chat_id": chat_id})
        return True


def get_all_chats():
    r = list(lockurl.find())
    if r:
        return r
    else:
        return False


def get_session(chat_id):
    stark = lockurl.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        return stark


async def is_nightmode_indb(chat_id: int) -> bool:
    chat = await nightdb.find_one({"chat_id": chat_id})
    if not chat:
        return True
    return False


async def add_nightmode(chat_id: int):
    is_antiservice = await is_nightmode_indb(chat_id)
    if is_antiservice:
        return
    return await nightdb.delete_one({"chat_id": chat_id})


async def rmnightmode(chat_id: int):
    is_antiservice = await is_nightmode_indb(chat_id)
    if not is_antiservice:
        return
    return await nightdb.insert_one({"chat_id": chat_id})

def get_all_chat_id():
    r = list(nightdb.find())
    if r:
        return r
    else:
        return False

def obj_to_str(obj):
    if not obj:
        return False
    string = codecs.encode(pickle.dumps(obj), "base64").decode()
    return string


def str_to_obj(string: str):
    obj = pickle.loads(codecs.decode(string.encode(), "base64"))
    return obj

#1
async def start_restart_stage(chat_id: int, message_id: int):
    await restart_stagedb.update_one(
        {"something": "something"},
        {
            "$set": {
                "chat_id": chat_id,
                "message_id": message_id,
            }
        },
        upsert=True,
    )
#2
async def is_captcha_on(chat_id: int) -> bool:
    chat = await captchadb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def captcha_off(chat_id: int):
    is_captcha = await is_captcha_on(chat_id)
    if not is_captcha:
        return
    return await captchadb.delete_one({"chat_id": chat_id})


async def captcha_on(chat_id: int):
    is_captcha = await is_captcha_on(chat_id)
    if is_captcha:
        return
    return await captchadb.insert_one({"chat_id": chat_id})


async def has_solved_captcha_once(chat_id: int, user_id: int):
    has_solved = await solved_captcha_db.find_one(
        {"chat_id": chat_id, "user_id": user_id}
    )
    return bool(has_solved)


async def save_captcha_solved(chat_id: int, user_id: int):
    return await solved_captcha_db.update_one(
        {"chat_id": chat_id},
        {"$set": {"user_id": user_id}},
        upsert=True,
    )

async def update_captcha_cache(captcha_dict):
    pickle = obj_to_str(captcha_dict)
    await captcha_cachedb.delete_one({"captcha": "cache"})
    if not pickle:
        return
    await captcha_cachedb.update_one(
        {"captcha": "cache"},
        {"$set": {"pickled": pickle}},
        upsert=True,
    )


async def get_captcha_cache():
    cache = await captcha_cachedb.find_one({"captcha": "cache"})
    if not cache:
        return []
    return str_to_obj(cache["pickled"])

#3
async def is_flood_on(chat_id: int) -> bool:
    chat = await flood_toggle_db.find_one({"chat_id": chat_id})
    if not chat:
        return True
    return False


async def flood_on(chat_id: int):
    is_flood = await is_flood_on(chat_id)
    if is_flood:
        return
    return await flood_toggle_db.delete_one({"chat_id": chat_id})


async def flood_off(chat_id: int):
    is_flood = await is_flood_on(chat_id)
    if not is_flood:
        return
    return await flood_toggle_db.insert_one({"chat_id": chat_id})

#4
async def get_warns_count() -> dict:
    chats = warnsdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return {}
    chats_count = 0
    warns_count = 0
    for chat in await chats.to_list(length=100000000):
        for user in chat["warns"]:
            warns_count += chat["warns"][user]["warns"]
        chats_count += 1
    return {"chats_count": chats_count, "warns_count": warns_count}


async def get_warns(chat_id: int) -> Dict[str, int]:
    warns = await warnsdb.find_one({"chat_id": chat_id})
    if not warns:
        return {}
    return warns["warns"]


async def get_warn(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    warns = await get_warns(chat_id)
    if name in warns:
        return warns[name]


async def add_warn(chat_id: int, name: str, warn: dict):
    name = name.lower().strip()
    warns = await get_warns(chat_id)
    warns[name] = warn

    await warnsdb.update_one(
        {"chat_id": chat_id}, {"$set": {"warns": warns}}, upsert=True
    )


async def remove_warns(chat_id: int, name: str) -> bool:
    warnsd = await get_warns(chat_id)
    name = name.lower().strip()
    if name in warnsd:
        del warnsd[name]
        await warnsdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"warns": warnsd}},
            upsert=True,
        )
        return True
    return False

#5
async def is_antiservice_on(chat_id: int) -> bool:
    chat = await antiservicedb.find_one({"chat_id": chat_id})
    if not chat:
        return True
    return False


async def antiservice_on(chat_id: int):
    is_antiservice = await is_antiservice_on(chat_id)
    if is_antiservice:
        return
    return await antiservicedb.delete_one({"chat_id": chat_id})


async def antiservice_off(chat_id: int):
    is_antiservice = await is_antiservice_on(chat_id)
    if not is_antiservice:
        return
    return await antiservicedb.insert_one({"chat_id": chat_id})

#6
# To on / off / get anti functions
async def set_anti_func(chat_id, status, mode):
    anti_f = await nexaub_antif.find_one({"_id": chat_id})
    if anti_f:
        await nexaub_antif.update_one({"_id": chat_id}, {"$set": {"status": status, "mode": mode}})
    else:
        await nexaub_antif.insert_one({"_id": chat_id, "status": status, "mode": mode})

async def get_anti_func(chat_id):
    anti_f = await nexaub_antif.find_one({"_id": chat_id})
    if not anti_f:
        return None
    else:
        snm = [anti_f["status"], anti_f["mode"]]
        return snm

async def del_anti_func(chat_id):
    anti_f = await nexaub_antif.find_one({"_id": chat_id})
    if anti_f:
        await nexaub_antif.delete_one({"_id": chat_id})
        return True
    else:
        return False
    
    
#7
async def clean_restart_stage() -> dict:
    data = await restart_stagedb.find_one({"something": "something"})
    if not data:
        return {}
    await restart_stagedb.delete_one({"something": "something"})
    return {
        "chat_id": data["chat_id"],
        "message_id": data["message_id"],
    }
async def int_to_alpha(user_id: int) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text


async def alpha_to_int(user_id_alphabet: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    user_id = ""
    for i in user_id_alphabet:
        index = alphabet.index(i)
        user_id += str(index)
    user_id = int(user_id)
    return user_id

async def get_filters_count() -> dict:
    chats = filtersdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return {}
    chats_count = 0
    filters_count = 0
    for chat in await chats.to_list(length=1000000000):
        filters_name = await get_filters_names(chat["chat_id"])
        filters_count += len(filters_name)
        chats_count += 1
    return {
        "chats_count": chats_count,
        "filters_count": filters_count,
    }


async def _get_filters(chat_id: int) -> Dict[str, int]:
    _filters = await filtersdb.find_one({"chat_id": chat_id})
    if not _filters:
        return {}
    return _filters["filters"]


async def get_filters_names(chat_id: int) -> List[str]:
    _filters = []
    for _filter in await _get_filters(chat_id):
        _filters.append(_filter)
    return _filters


async def get_filter(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _filters = await _get_filters(chat_id)
    if name in _filters:
        return _filters[name]
    return False


async def save_filter(chat_id: int, name: str, _filter: dict):
    name = name.lower().strip()
    _filters = await _get_filters(chat_id)
    _filters[name] = _filter
    await filtersdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"filters": _filters}},
        upsert=True,
    )


async def delete_filter(chat_id: int, name: str) -> bool:
    filtersd = await _get_filters(chat_id)
    name = name.lower().strip()
    if name in filtersd:
        del filtersd[name]
        await filtersdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"filters": filtersd}},
            upsert=True,
        )
        return True
    return False

async def is_using_rose(user_id):
    chat = usersdb.find_one({"user_id": user_id})
    if not chat:
        return False
    return True

async def add_user(user_id):
    is_using = await is_using_rose(user_id)
    if is_using:
        return
    return await usersdb.insert_one({"user_id": user_id}) 

async def remove_user(user_id):
    is_using = await is_using_rose(user_id)
    if not is_using:
        return
    return await usersdb.delete_one({"user_id": user_id})

async def is_rose_in_groups(group_id):
    chat = groupsdb.find_one({"group_id": group_id})
    if not chat:
        return False
    return True

async def add_group(group_id):
    is_using = await is_rose_in_groups(group_id)
    if is_using:
        return
    return await groupsdb.insert_one({"group_id": group_id}) 

async def remove_group(group_id):
    is_using = await is_rose_in_groups(group_id)
    if not is_using:
        return
    return await groupsdb.delete_one({"group_id": group_id})

async def all_users() -> list:
    chats = usersdb.find({})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list

async def all_groups() -> list:
    chats = usersdb.find({})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list
from TGN.mongo import db
