# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Limit**

๏ **Perintah:** `limit`
◉ **Keterangan:** Periksa Anda terbatas atau tidak.
"""

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import ayra_cmd


@ayra_cmd(pattern="(L|l)imit$")
async def demn(ayra):
    chat = "@SpamBot"
    msg = await ayra.eor("Memeriksa Jika Anda Terbatas...")
    async with ayra.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await ayra.client.send_read_acknowledge(chat)
        except YouBlockedUserError:
            await msg.edit("Silakan Buka Blokir @SpamBot ")
            return
        await msg.edit(f"~ {response.message.message}")
