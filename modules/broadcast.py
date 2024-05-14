
# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ Bantuan Untuk Broadcast

๏ Perintah: Gcast
◉ Keterangan: Kirim Pesan Ke Semua Grup Anda.

๏ Perintah: Gucast
◉ Keterangan: Kirim Pesan Ke Semua Pengguna Pribadi.

๏ Perintah Addbl
◉ Keterangan: Tambahkan Grup Ke Dalam Blacklist Gcast.

๏ Perintah: Delbl
◉ Keterangan: Hapus Grup Dari Daftar Blacklist Gcast.

๏ Perintah: Blchat
◉ Keterangan: Melihat Daftar Blacklist Gcast.
"""
import asyncio

from Ayra.dB import DEVS
from Ayra.dB.gcast_blacklist_db import add_gblacklist, list_bl, rem_gblacklist
from Ayra.dB.broadcast_db import get_vars
from Ayra.fns.tools import create_tl_btn, format_btn, get_msg_button
from telethon.errors.rpcerrorlist import FloodWaitError

from . import *
from ._inline import something


@ayra_cmd(pattern="[gG][c][a][s][t]( (.*)|$)", fullsudo=False)
async def gcast(event):
    emot_1 = await get_vars(Client.me.id, "EMOJI_PROSES")
    emot_2 = await get_vars(Client.me.id, "EMOJI_CEKLIS")
    emot_3 = await get_vars(Client.me.id, "EMOJI_GAGAL")
    emot_proses = emot_1 if emot_1 else "6113844439292054570"
    emot_ceklis = emot_2 if emot_2 else "6113647841459047673"
    emot_gagal = emot_3 if emot_3 else "6113872536968104754"
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await eor(
            event, "`Berikan beberapa teks ke Globally Broadcast atau balas pesan..`"
        )
    kk = await event.eor("<b><emoji id={emot_proses}>⏳</emoji>Sebentar Kalo Limit Jangan Salahin Dareen Ya Kontol...")
    er = 0
    done = 0
    err = ""
    chat_blacklist = udB.get_key("GBLACKLISTS") or []
    chat_blacklist.append(-1002109872719)
    udB.set_key("GBLACKLISTS", chat_blacklist)
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            
            if chat not in chat_blacklist and chat not in NOSPAM_CHAT:
                try:
                    await event.client.send_message(chat, msg)
                    done += 1
                except FloodWaitError as fw:
                    await asyncio.sleep(fw.seconds + 10)
                    try:
                        await event.client.send_message(
                                chat, msg)
                        done += 1
                    except Exception as rr:
                        err += f"• {rr}\n"
                        er += 1
                except BaseException as h:
                    err += f"• {str(h)}" + "\n"
                    er += 1
    await kk.edit(f"**<b><emoji id={emot_ceklis}>✅️</emoji>Berhasil Terkirim :  {done} Grup Chat\n<b><emoji id={emot_gagal}>❎️</emoji>Gagal : {er} Grup Chat**")


@ayra_cmd(pattern="[gG][u][c][a][s][t]( (.*)|$)", fullsudo=False)
async def gucast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await eor(
            event, "`Berikan beberapa teks ke Globally Broadcast atau balas pesan..`"
        )
    kk = await event.eor("`Sebentar Kalo Limit Jangan Salahin Dareen Ya Kontol...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(f"Berhasil di {done} obrolan, kesalahan {er} obrolan")


@ayra_cmd(pattern="addbl")
@register(incoming=True, from_users=DEVS, pattern=r"^Addbl")
async def blacklist_(event):
    await gblacker(event, "add")


@ayra_cmd(pattern="delbl")
async def ungblacker(event):
    await gblacker(event, "remove")


@ayra_cmd(pattern="blchat")
async def chatbl(event):
    id = event.chat_id
    if xx := list_bl(id):
        sd = "**❏ Daftar Blacklist Gcast**\n\n"
        return await event.eor(sd + xx)
    await event.eor("**Belum ada daftar**")


async def gblacker(event, type_):
    args = event.text.split()
    if len(args) > 2:
        return await event.eor("**Gunakan Format:**\n `delbl` or `addbl`")
    chat_id = None
    chat_id = int(args[1]) if len(args) == 2 else event.chat_id
    if type_ == "add":
        add_gblacklist(chat_id)
        await event.eor(f"**Berhasil Di Tambahkan Ke Daftar Hitam**\n`{chat_id}`")
    elif type_ == "remove":
        rem_gblacklist(chat_id)
        await event.eor(f"**Dihapus dari BL-GCAST**\n`{chat_id}`")
