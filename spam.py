# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -
• `{i}spam <no of msgs> <your msg>`
    spams chat, the current limit for this is from 1 to 99.

• `{i}bigspam <no of msgs> <your msg>`
    Spams chat, the current limit is above 100.

• `{i}picspam <no of spam> <reply to media>`
    Spam media.

• `{i}delayspam <delay time> <count> <msg>`
    Spam chat.

"""

from asyncio import wait, sleep
import os
from . import *


@ultroid_cmd(pattern="tspam")
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()

@ultroid_cmd(pattern=f"mspam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
                               
@ultroid_cmd(pattern=f"bigspam")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        
        
@ultroid_cmd(pattern=f"picspam")
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        reply = await e.get_reply_message()
        message = e.text
        text = message.split()
        counter = int(text[1])
        media = await e.client.download_media(reply)
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, media)
        os.remove(media)
        await e.delete()
        
@ultroid_cmd(pattern=f"delayspam (.*)")
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
