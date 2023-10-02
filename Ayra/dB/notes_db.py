# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

from .. import udB

def get_stuff():
    return udB.get_key("NOTE") or {}


def add_note(user, word, msg, media, button):
    ok = get_stuff()
    if ok.get(int(user)):
        ok[int(user)].update({word: {"msg": msg, "media": media, "button": button}})
    else:
        ok.update({int(user): {word: {"msg": msg, "media": media, "button": button}}})
    udB.set_key("NOTE", ok)


def rem_note(user, word):
    ok = get_stuff()
    if ok.get(int(user)) and ok[int(user)].get(word):
        ok[int(user)].pop(word)
        return udB.set_key("NOTE", ok)


def rem_all_note(user):
    ok = get_stuff()
    if ok.get(int(user)):
        ok.pop(int(user))
        return udB.set_key("NOTE", ok)


def get_notes(user, word):
    ok = get_stuff()
    if ok.get(int(user)) and ok[int(user)].get(word):
        return ok[int(user)][word]


def list_note(user):
    ok = get_stuff()
    if ok.get(int(user)):
        return "".join(f"**๏** `{z}`\n" for z in ok[user])
