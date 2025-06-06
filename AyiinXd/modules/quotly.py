# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from os import remove
from secrets import choice

from telethon.tl.functions.users import GetFullUserRequest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.ayiin.misc import create_quotly
from Stringyins import get_string

from .carbon import all_col


@ayiin_cmd(pattern="q( (.*)|$)")
async def quotly(event):
    match = event.pattern_match.group(1).strip()
    if not event.is_reply:
        return await eod(event, get_string("gban_8"))
    msg = await eor(event, get_string("com_1"))
    reply = await event.get_reply_message()
    replied_to, reply_ = None, None
    if match:
        spli_ = match.split(maxsplit=1)
        if (spli_[0] in ["r", "reply"]) or (
            spli_[0].isdigit() and int(spli_[0]) in range(1, 21)
        ):
            if spli_[0].isdigit():
                if not event.client._bot:
                    reply_ = await event.client.get_messages(
                        event.chat_id,
                        min_id=event.reply_to_msg_id - 1,
                        reverse=True,
                        limit=int(spli_[0]),
                    )
                else:
                    id_ = reply.id
                    reply_ = []
                    for msg_ in range(id_, id_ + int(spli_[0])):
                        msh = await event.client.get_messages(event.chat_id, ids=msg_)
                        if msh:
                            reply_.append(msh)
            else:
                replied_to = await reply.get_reply_message()
            try:
                match = spli_[1]
            except IndexError:
                match = None
    user = None
    if not reply_:
        reply_ = reply
    if match:
        match = match.split(maxsplit=1)
    if match:
        if match[0].startswith("@") or match[0].isdigit():
            try:
                match_ = await event.client(GetFullUserRequest(match[0]))
                user = await event.client.get_entity(match_)
            except ValueError:
                pass
            match = match[1] if len(match) == 2 else None
        else:
            match = match[0]
    if match == "random":
        match = choice(all_col)
    try:
        file = await create_quotly(reply_, bg=match, reply=replied_to, sender=user)
    except Exception as er:
        return await msg.edit(get_string("error_1").format(er))
    message = await reply.reply("Quotly by 𝗟𝘰𝘦𝘻𝘴𝘬𝘺-Userbot", file=file)
    remove(file)
    await msg.delete()
    return message


CMD_HELP.update(
    {
        "quotly": f"**Plugin : **`quotly`\
        \n\n  »  **Perintah :** `{cmd}q`\
        \n  »  **Kegunaan : **Membuat pesan menjadi sticker dengan random background.\
        \n\n  »  **Perintah :** `{cmd}q` <angka>\
        \n  »  **Kegunaan : **Membuat pesan menjadi sticker dengan custom jumlah pesan yang diberikan.\
        \n\n  »  **Perintah :** `{cmd}q` <warna>\
        \n  »  **Kegunaan : **Membuat pesan menjadi sticker dengan custom warna background yang diberikan.\
        \n\n  »  **Perintah :** `{cmd}q` <username>\
        \n  »  **Kegunaan : **Membuat pesan menjadi sticker dengan custom username user tele yang diberikan.\
    "
    }
)
