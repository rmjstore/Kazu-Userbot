# repack by blue. #
""" Userbot start point """


import sys
from importlib import import_module
from platform import python_version

from pytgcalls import __version__ as pytgcalls
from telethon import version
from telethon.tl.alltlobjects import LAYER
from AyiinXd.ayiin.events import ajg
from AyiinXd import BOT_TOKEN, bot
from AyiinXd import BOT_VER as ubotversion
from AyiinXd import BOTLOG_CHATID, LOGS, LOOP, bot
from AyiinXd.clients import ayiin_userbot_on, multiayiin
from AyiinXd.core.git import git
from AyiinXd.modules import ALL_MODULES
from AyiinXd.ayiin import AyiinDB, HOSTED_ON, autobot, autopilot, ayiin_version


try:
    for module_name in ALL_MODULES:
        imported_module = import_module(f"AyiinXd.modules.{module_name}")
    adB = AyiinDB()
    client = multiayiin()
    git()
    LOGS.info(f"Python Version - {python_version()}")
    LOGS.info(f"Telethon Version - {version.__version__} [Layer: {LAYER}]")
    LOGS.info(f"PyTgCalls Version - {pytgcalls}")
    LOGS.info(f"Userbot Version - {ubotversion} •[{adB.name}]•")
    LOGS.info(f"rmj Version - {ayiin_version} •[{HOSTED_ON}]•")
    LOGS.info("[✨ BERHASIL DIAKTIFKAN! ✨]")
except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
    pass
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


LOOP.run_until_complete(ayiin_userbot_on())
LOOP.run_until_complete(ajg())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(autopilot())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
