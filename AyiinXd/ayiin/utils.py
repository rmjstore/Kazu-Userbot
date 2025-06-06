# Credits: @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
# autopilot by @kenkan

import asyncio
import importlib
import logging
import random
import sys
from pathlib import Path
from random import randint


import heroku3
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors import ChannelsTooMuchError
from telethon.tl.functions.channels import CreateChannelRequest, EditPhotoRequest
from telethon.tl.types import ChatPhotoEmpty, InputChatUploadedPhoto
from telethon.utils import get_peer_id

from AyiinXd import (
    BOT_TOKEN,
    BOTLOG_CHATID,
    CMD_HELP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    LOGS,
    bot,
)

from .tools import download_file


heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


async def autopilot():
    LOGS.info("SEDANG MEMBUAT GROUP LOG USERBOT UNTUK ANDA")
    if BOTLOG_CHATID and str(BOTLOG_CHATID).startswith("-100"):
        return
    y = []  # To Refresh private ids
    async for x in bot.iter_dialogs():
        y.append(x.id)
    if BOTLOG_CHATID:
        try:
            await bot.get_entity(int("BOTLOG_CHATID"))
            return
        except BaseException:
            del heroku_var["BOTLOG_CHATID"]
    try:
        r = await bot(
            CreateChannelRequest(
                title="botlogs.-rmj-Userbot",
                about="support channel @roemahjaseb",
                megagroup=True,
            ),
        )
    except ChannelsTooMuchError:
        LOGS.info(
            "Channel dan Group Lu Banyak Tod, Hapus Salah Satu Dan Restart Lagi"
        )
        exit(1)
    except BaseException:
        LOGS.info(
            "Terjadi kesalahan, Buat sebuah grup lalu isi id nya di config var BOTLOG_CHATID."
        )
        exit(1)
    chat = r.chats[0]
    channel = get_peer_id(chat)
    if isinstance(chat.photo, ChatPhotoEmpty):
        photo = await download_file(
            "https://telegra.ph/file62e6065830dd426a/roemah_jaseb.jpg", "photoyins.jpg"
        )
        ll = await bot.upload_file(photo)
        try:
            await bot(
                EditPhotoRequest(int(channel), InputChatUploadedPhoto(ll))
            )
        except BaseException as er:
            LOGS.exception(er)
    if not str(chat.id).startswith("-100"):
        heroku_var["BOTLOG_CHATID"] = f"-100{str(chat.id)}"
    else:
        heroku_var["BOTLOG_CHATID"] = str(chat.id)


async def autobot():
    if BOT_TOKEN:
        return
    await bot.start()
    await asyncio.sleep(15)
    await bot.send_message(
        BOTLOG_CHATID, "**creating assistant bot on @BotFather**"
    )
    LOGS.info("TUNGGU SEBENTAR SAYANG. SEDANG MEMBUAT ASSISTANT BOT UNTUK KAMU")
    who = await bot.get_me()
    name = f"{who.first_name} Assistant Bot"
    if who.username:
        username = f"{who.username}_bot"
    else:
        username = f"rmj{(str(who.id))[5:]}bot"
    bf = "@BotFather"
    await bot(UnblockRequest(bf))
    await bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
        )
        sys.exit(1)
    await bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
            )
            sys.exit(1)
    filogo = random.choice(
          [
              "https://telegra.ph/file/00b635e340db8b85be11b.jpg", 
              "https://telegra.ph/file/00b635e340db8b85be11b.jpg",
          ]
    )
    await bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    await bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = f"rmj{str(who.id)[6:]}{ran}bot"
        await bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            await bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, "Search")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_file(bf, filogo)
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"awesome bot by {who.first_name}")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(
                bf, f"made for you from roemahjaseb"
            )
            await bot.send_message(
                BOTLOG_CHATID,
                f"**complete creating bot @{username}**",
            )
            LOGS.info(
                f"BERHASIL MEMBUAT ASSISTANT BOT KAMU DENGAN USERNAME @{username}")
            await bot.send_message(
                BOTLOG_CHATID,
                "**restarting bot. support @roemahjaseb**",
            )
            heroku_var["BOT_TOKEN"] = token
            heroku_var["BOT_USERNAME"] = f"@{username}"
        else:
            LOGS.info(
                "Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot"
            )
            sys.exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        await bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, "Search")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setuserpic")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_file(bf, filogo)
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setabouttext")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"awesome bot by {who.first_name}")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setdescription")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(
            bf, f"made for you from roemahjaseb"
        )
        await bot.send_message(
            BOTLOG_CHATID,
            f"**complete creating bot @{username}**",
        )
        LOGS.info(
            f"BERHASIL MEMBUAT ASSISTANT BOT KAMU DENGAN USERNAME @{username}")
        await bot.send_message(
            BOTLOG_CHATID,
            "**restarting bot. support @roemahjaseb**",
        )
        heroku_var["BOT_TOKEN"] = token
        heroku_var["BOT_USERNAME"] = f"@{username}"
    else:
        LOGS.info(
            "Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot"
        )
        sys.exit(1)


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"AyiinXd/modules/{shortname}.py")
        name = f"AyiinXd.modules.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info(f"Successfully imported {shortname}")
    else:

        path = Path(f"AyiinXd/modules/{shortname}.py")
        name = f"AyiinXd.modules.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.CMD_HELP = CMD_HELP
        mod.logger = logging.getLogger(shortname)
        spec.loader.exec_module(mod)
        # for imports
        sys.modules[f"AyiinXd.modules.{shortname}"] = mod
        LOGS.info(f"Successfully imported {shortname}")


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"AyiinXd/modules/assistant/{shortname}.py")
        name = f"AyiinXd.modules.assistant.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Starting Your Assistant Bot.")
        LOGS.info(f"Assistant Sucessfully imported {shortname}")
    else:
        path = Path(f"AyiinXd/modules/assistant/{shortname}.py")
        name = f"AyiinXd.modules.assistant.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules[f"AyiinXd.modules.assistant{shortname}"] = mod
        LOGS.info(f"Assistant Successfully imported{shortname}")


def remove_plugin(shortname):
    try:
        try:
            for i in CMD_HELP[shortname]:
                bot.remove_event_handler(i)
            del CMD_HELP[shortname]

        except BaseException:
            name = f"AyiinXd.modules.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError
