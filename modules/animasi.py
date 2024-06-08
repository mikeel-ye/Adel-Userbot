# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Animasi**

๏ **Perintah:** `skull`
◉ **Keterangan:** Coba sendiri.

๏ **Perintah:** `wlc`
◉ **Keterangan:** Coba sendiri.

๏ **Perintah:** `klb`
◉ **Keterangan:** Coba sendiri.

๏ **Perintah:** `fucek`
◉ **Keterangan:** Coba sendiri.

๏ **Perintah:** `ror`
◉ **Keterangan:** Coba sendiri.
"""

from . import *


@ayra_cmd(pattern="skull(?: |$)(.*)")
async def _(event):
    await event.edit(
        "███████████████████████████\n"
        "███████▀▀▀░░░░░░░▀▀▀███████\n"
        "████▀░░░░░░░░░░░░░░░░░▀████\n"
        "███│░░░░░░░░░░░░░░░░░░░│███\n"
        "██▌│░░░░░░░░░░░░░░░░░░░│▐██\n"
        "██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n"
        "██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n"
        "██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n"
        "██▌░│██████▌░░░▐██████│░▐██\n"
        "███░│▐███▀▀░░▄░░▀▀███▌│░███\n"
        "██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n"
        "██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n"
        "████▄─┘██▌░░░░░░░▐██└─▄████\n"
        "█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n"
        "████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n"
        "█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n"
        "███████▄░░░░░░░░░░░▄███████\n"
        "██████████▄▄▄▄▄▄▄██████████\n"
        "███████████████████████████\n"
    )


@ayra_cmd(pattern="wlc(?: |$)(.*)")
async def _(event):
    await event.edit(
        "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
        "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
        "█░░║║║╠─║─║─║║║║║╠─░░█\n"
        "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
        "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
    )


@ayra_cmd(pattern="klb(?: |$)(.*)")
async def _(event):
    await event.edit(
        "   ╚⊙ ⊙╝..\n"
        "   ╚═(███)═╝\n"
        "    ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "    ╚═(███)═╝ \n"
        "    ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "      ╚═(█)═╝\n"
    )


@ayra_cmd(pattern="fucek(?: |$)(.*)")
async def _(event):
    await event.edit(
        "░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "██████▄███▄████░░███▄░░░░░░░\n"
        "▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░\n"
        "▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░\n"
        "▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░\n"
    )

@ayra_cmd(pattern="ror(?: |$)(.*)")
async def _(event):
    xx = await eor(event, "**ROOORRR**")
    sleep(2)
    await xx.edit("**ROOORRRR AAHHHH**")
    sleep(1)
    await xx.edit("**ROOORRRR AAHHHH AAHHH**")
    sleep(1)
    await xx.edit("**ROOORRRR AAHHHH AAHHH AAHHH**")
    sleep(1)
    await xx.edit("**ROOORRRR AAHHHH AAHHH AAHHH AAHHH**")