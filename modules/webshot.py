# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Webshot**

๏ **Perintah:** `ss` <link>
◉ **Keterangan:** Dapatkan screenshot dari link tersebut
"""


from . import *


@ayra_cmd(pattern="ss(?:\\s+(.*))?")
async def webshot(e):
    ajg = await e.eor("`Processing...`")
    try:
        user_link = e.pattern_match.group(1).strip()
        if not user_link:
            await e.eor(
                "`Masukkan URL situs web yang ingin diambil tangkapan layarnya.`"
            )
            return
        full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
        await ajg.delete()
        await e.client.send_file(
            e.chat_id,
            full_link,
            caption=f"**Tangkapan layar halaman** {user_link}",
        )
    except Exception as error:
        await e.eor(f"**Terjadi kesalahan:** `{error}`")
